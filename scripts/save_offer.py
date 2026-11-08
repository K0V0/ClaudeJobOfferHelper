#!/usr/bin/env python3
"""Saves a job offer word for word (offer.md) and as printed page (offer-page.pdf) into its offer folder.

Usage: save-offer <url> [--folder <offer folder>] [--pdf-only]

Exit codes: 0 = saved, 2 = offer text could not be read, nothing was written.
"""
import argparse
import datetime
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup

SCRIPTS = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))  # _MEIPASS = unpacked prebuilt executable
sys.path.insert(0, str(SCRIPTS))

from common import generic_extract  # noqa: E402

DATA = Path.home() / "JobOfferHelper"  # plugin folder is replaced on every update
OFFER_ROOT = DATA / "offer-results"
TEXT_MARKER = "## Original text"
MIN_TEXT_LENGTH = 400
BROWSER_COMMANDS = ("google-chrome", "google-chrome-stable", "chrome", "chromium-browser", "chromium",
                    "microsoft-edge", "microsoft-edge-stable", "msedge", "brave-browser")
MAC_BROWSERS = ("Google Chrome", "Chromium", "Microsoft Edge", "Brave Browser")
WINDOWS_BROWSERS = ("Google/Chrome/Application/chrome.exe", "Chromium/Application/chrome.exe",
                    "Microsoft/Edge/Application/msedge.exe", "BraveSoftware/Brave-Browser/Application/brave.exe")
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
TRACKING_PARAMS = {"searchid", "rps", "impressionid", "position", "pagenum", "refid", "trackingid", "search_id", "lang"}
PRINT_CSS = """
:is(#cc_div, #cc-main, #onetrust-consent-sdk, #CybotCookiebotDialog, [id*="cookie" i], [class*="cookie" i],
[id*="consent" i], [class*="consent" i]):not(html, body) { display: none !important; }
.show-more-less-html__markup { -webkit-line-clamp: unset !important; max-height: none !important; overflow: visible !important; }
html, body { overflow: visible !important; height: auto !important; }
"""


def load_portals():
    portals = []
    for path in [*sorted(SCRIPTS.glob("*/extract.py")), *sorted((DATA / "portals").glob("*/extract.py"))]:
        spec = importlib.util.spec_from_file_location(f"portal_{path.parent.name}", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        portals.append((path.parent.name, module))
    return portals


def find_portal(url):
    host = (urlsplit(url).hostname or "").lower()
    for name, module in load_portals():
        if any(host == known or host.endswith("." + known) for known in module.HOSTS):
            return name, module
    return "generic", None


def canonical_url(url):
    parts = urlsplit(url.strip())
    query = [
        (key, value)
        for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if key.lower() not in TRACKING_PARAMS and not key.lower().startswith("utm_")
    ]
    return urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip("/"), urlencode(query), ""))


def browser_locations():
    """macOS and Windows browsers are usually not on PATH."""
    for name in MAC_BROWSERS:
        for root in (Path("/Applications"), Path.home() / "Applications"):
            yield root / f"{name}.app" / "Contents" / "MacOS" / name
    roots = [os.environ[name] for name in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA") if os.environ.get(name)]
    for executable in WINDOWS_BROWSERS:
        for root in roots:
            yield Path(root) / executable


def find_browser():
    on_path = next((path for path in map(shutil.which, BROWSER_COMMANDS) if path), None)
    return on_path or next((str(path) for path in browser_locations() if path.is_file()), None)


def browser_environment():
    """Prebuilt executable points Linux to its own libraries, the browser needs the system ones."""
    environment = dict(os.environ)
    if getattr(sys, "frozen", False):
        environment.pop("LD_LIBRARY_PATH", None)
        if "LD_LIBRARY_PATH_ORIG" in environment:
            environment["LD_LIBRARY_PATH"] = environment["LD_LIBRARY_PATH_ORIG"]
    return environment


def run_browser(arguments):
    browser = find_browser()
    if not browser:
        return None
    # Chrome on Windows can hold its profile files for a moment after it exits
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as profile:
        command = [browser, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={profile}",
                   "--virtual-time-budget=9000", *arguments]
        try:
            return subprocess.run(command, capture_output=True, timeout=90, env=browser_environment())
        except subprocess.TimeoutExpired:
            return None


def fetch_plain(url):
    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "cs,sk;q=0.9,en;q=0.8"}, timeout=30)
    except requests.RequestException:
        return None, url, "connection failed"
    response.encoding = "utf-8"
    if response.status_code >= 400:
        return None, response.url, f"HTTP {response.status_code}"
    return response.text, response.url, None


def fetch_rendered(url):
    result = run_browser(["--dump-dom", url])
    if result is None or result.returncode != 0:
        return None
    return result.stdout.decode("utf-8", errors="replace")


def is_usable(offer):
    return bool(offer) and len(offer["text"]) >= MIN_TEXT_LENGTH


def extract(page, portal, module):
    soup = BeautifulSoup(page, "html.parser")
    offer = module.extract(soup) if module else None
    if is_usable(offer):
        return offer, portal
    return generic_extract(soup), "generic"


def scrape(url, portal, module):
    """Plain request is cheap, the browser is used only when the page needs JavaScript or refuses the request."""
    plain, final_url, problem = fetch_plain(url)
    fallback = None
    for source in (lambda: plain, lambda: fetch_rendered(url)):
        page = source()
        if not page:
            continue
        offer, used = extract(page, portal, module)
        if is_usable(offer) and used == portal:
            return offer, used, final_url, page, None
        if is_usable(offer):
            fallback = fallback or (offer, used, final_url, page, None)
    return fallback or (None, portal, final_url, plain, problem or "offer text not found on the page")


def slug(value, limit):
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    words = re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")
    if len(words) > limit:
        words = words[:limit + 1].rpartition("-")[0] or words[:limit]
    return words or "unknown"


def company_slug(company):
    return slug(re.sub(r"[,\s]+(s\.?\s?r\.?\s?o\.?|spol\..*|a\.?\s?s\.?|k\.?\s?s\.?|gmbh|inc\.?|ltd\.?)\s*$", "", company, flags=re.I), 40)


def position_slug(title):
    return slug(re.sub(r"\((m/|ž/|muž|f/|w/|m/ž|all)[^)]*\)", "", title, flags=re.I), 50)


def find_existing_folder(urls):
    wanted = {canonical_url(url) for url in urls}
    for path in sorted(OFFER_ROOT.glob("*/offer.md")):
        match = re.search(r"^- Link: (\S+)", path.read_text(encoding="utf-8"), flags=re.M)
        if match and canonical_url(match.group(1)) in wanted:
            return path.parent
    return None


def free_name(folder, stem, suffix, today):
    candidate = folder / f"{stem}-{today}{suffix}"
    number = 2
    while candidate.exists():
        candidate = folder / f"{stem}-{today}-{number}{suffix}"
        number += 1
    return candidate


def squeeze(text):
    return re.sub(r"\s+", " ", text).strip()


def offer_file(folder, text, today):
    """offer.md is written once, changed text goes next to it, the same text writes nothing."""
    existing = sorted(folder.glob("offer*.md"))
    if not existing:
        return folder / "offer.md"
    if any(squeeze(text) in squeeze(path.read_text(encoding="utf-8")) for path in existing):
        return None
    return free_name(folder, "offer", ".md", today)


def render(offer, url, final_url, portal, today):
    fields = [("Link", url), ("Final link", final_url if canonical_url(final_url) != canonical_url(url) else ""),
              ("Company", offer["company"]), ("Location", offer["location"]), ("Salary", offer["salary"]),
              ("Posted", offer["posted"]), ("Valid through", offer["valid_through"]), ("Saved", today), ("Extractor", portal)]
    header = "\n".join(f"- {name}: {value}" for name, value in fields if value)
    return f"# {offer['title']}\n\n{header}\n\n{TEXT_MARKER}\n\n{offer['text']}\n"


def print_pdf(page, base_url, target):
    """Prints a local copy without scripts, on the live page cookie dialogs cover the offer and LinkedIn redirects to login."""
    soup = BeautifulSoup(page, "html.parser")
    for script in soup.find_all("script"):
        script.decompose()
    for link in soup.find_all("link"):  # local copy has no origin, these attributes would block the stylesheets
        link.attrs.pop("crossorigin", None)
        link.attrs.pop("integrity", None)
    head = soup.head or soup
    style = soup.new_tag("style")
    style.string = PRINT_CSS
    head.insert(0, soup.new_tag("base", href=base_url))
    head.insert(0, soup.new_tag("meta", charset="utf-8"))
    head.append(style)
    target = target.resolve()
    # next to the target, snap Chromium on Ubuntu has its own /tmp and would not see the copy there
    with tempfile.TemporaryDirectory(dir=target.parent, ignore_cleanup_errors=True) as folder:
        copy = Path(folder) / "page.html"
        copy.write_text(str(soup), encoding="utf-8")
        result = run_browser(["--no-pdf-header-footer", f"--print-to-pdf={target}", copy.as_uri()])
    return result is not None and result.returncode == 0 and target.exists() and target.stat().st_size > 0


def save_pdf(page, base_url, folder, changed, today):
    target = folder / "offer-page.pdf"
    if target.exists():
        if not changed:
            return "unchanged"
        target = free_name(folder, "offer-page", ".pdf", today)
    if not find_browser():
        return "failed, no Chrome, Chromium, Edge or Brave found"
    if not page:
        return "failed"
    return target.name if print_pdf(page, base_url, target) else "failed"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url")
    parser.add_argument("--folder", type=Path, help="offer folder, default is existing folder of this link or a new one")
    parser.add_argument("--pdf-only", action="store_true", help="only print the page, for offers pasted by candidate")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # Windows console would crash on Czech letters
    today = datetime.date.today().isoformat()

    portal, module = find_portal(args.url)
    offer, portal, final_url, page, problem = scrape(args.url, portal, module)

    if args.pdf_only:
        if not args.folder:
            parser.error("--pdf-only needs --folder")
        args.folder.mkdir(parents=True, exist_ok=True)
        print(f"pdf: {save_pdf(page, final_url, args.folder, False, today)}")
        return 0

    if not offer:
        print(f"FAILED ({portal}): {problem}. Nothing was written.")
        return 2

    folder = args.folder or find_existing_folder([args.url, final_url])
    if folder is None:
        name = f"{today}-{company_slug(offer['company'] or 'unknown')}-{position_slug(offer['title'])}"
        folder = OFFER_ROOT / name
    folder.mkdir(parents=True, exist_ok=True)

    target = offer_file(folder, offer["text"], today)
    if target:
        target.write_text(render(offer, args.url, final_url, portal, today), encoding="utf-8")

    print(f"folder: {folder}")
    print(f"offer: {target.name if target else 'unchanged, nothing written'}")
    print(f"pdf: {save_pdf(page, final_url, folder, target is not None and target.name != 'offer.md', today)}")
    print(f"extractor: {portal}")
    print(f"title: {offer['title']} | company: {offer['company']} | text: {len(offer['text'])} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
