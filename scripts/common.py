"""Helpers shared by portal extractors: HTML to plain text and schema.org JobPosting parsing."""
import html
import json
import re

from bs4 import BeautifulSoup, NavigableString, Tag

SKIPPED_TAGS = {"script", "style", "svg", "noscript", "button", "form", "dialog", "iframe", "img"}
BLOCK_TAGS = {"p", "ul", "ol", "table", "blockquote", "pre", "section", "article"}
LINE_TAGS = {"div", "tr", "dd", "dt", "dl", "header", "footer", "main", "address"}
INVISIBLE = {0x200b: None, 0x200c: None, 0x200d: None, 0xfeff: None}


def _walk(node, out):
    for child in node.children:
        if isinstance(child, NavigableString):
            out.append(re.sub(r"\s+", " ", str(child)))
        elif isinstance(child, Tag) and child.name not in SKIPPED_TAGS:
            name = child.name
            if name == "br":  # html.parser nests following content into <br> when page closes it with </br>
                out.append("\n")
                _walk(child, out)
            elif name == "li":
                out.append("\n- ")
                _walk(child, out)
                out.append("\n")
            elif name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
                out.append("\n\n## ")
                _walk(child, out)
                out.append("\n\n")
            elif name in {"td", "th"}:
                _walk(child, out)
                out.append(" | ")
            elif name in BLOCK_TAGS or name in LINE_TAGS:
                separator = "\n\n" if name in BLOCK_TAGS else "\n"
                out.append(separator)
                _walk(child, out)
                out.append(separator)
            else:
                _walk(child, out)


def html_to_text(node):
    """Keeps every word of the node, only markup is replaced by headings, list dashes and line breaks."""
    out = []
    _walk(node, out)
    text = "".join(out).replace("\xa0", " ").translate(INVISIBLE)
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    text = re.sub(r"^(-|##)\n+(?=[^\n-])", r"\1 ", text, flags=re.M)
    text = re.sub(r"^(?:-|##)$\n?", "", text, flags=re.M)
    text = re.sub(r"( \| )+$", "", text, flags=re.M)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def fragment_to_text(markup):
    return html_to_text(BeautifulSoup(markup, "html.parser"))


def clean(node):
    return re.sub(r"\s+", " ", node.get_text(" ", strip=True).translate(INVISIBLE)).strip() if node else ""


def job_posting(soup):
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "", strict=False)
        except ValueError:
            continue
        items = data if isinstance(data, list) else data.get("@graph", [data])
        for item in items:
            kind = item.get("@type") if isinstance(item, dict) else None
            if kind == "JobPosting" or (isinstance(kind, list) and "JobPosting" in kind):
                return item
    return None


def _salary(posting):
    salary = posting.get("baseSalary")
    if not isinstance(salary, dict):
        return ""
    value = salary.get("value")
    if not isinstance(value, dict):
        return f"{value} {salary.get('currency', '')}".strip() if value else ""
    numbers = [value.get(key) for key in ("minValue", "value", "maxValue") if value.get(key)]
    amount = " - ".join(f"{number:,}".replace(",", " ") if isinstance(number, int) else str(number) for number in numbers)
    return " ".join(part for part in (amount, salary.get("currency"), value.get("unitText")) if part)


def _location(posting):
    places = posting.get("jobLocation") or []
    found = []
    for place in places if isinstance(places, list) else [places]:
        address = place.get("address") if isinstance(place, dict) else None
        if isinstance(address, dict):
            parts = [address.get(key) for key in ("streetAddress", "addressLocality", "addressCountry")]
            found.append(", ".join(str(part) for part in parts if part))
    if posting.get("jobLocationType") == "TELECOMMUTE":
        found.append("remote")
    return "; ".join(item for item in found if item)


def from_job_posting(posting):
    company = posting.get("hiringOrganization")
    return {
        "title": html.unescape(posting.get("title") or ""),
        "company": html.unescape((company.get("name") if isinstance(company, dict) else company) or ""),
        "location": _location(posting),
        "salary": _salary(posting),
        "posted": str(posting.get("datePosted") or "")[:10],
        "valid_through": str(posting.get("validThrough") or "")[:10],
        "text": fragment_to_text(html.unescape(posting.get("description") or "")),
    }


def from_alma_page(soup):
    """Layout of prace.cz and new jobs.cz: facts from JobPosting, text from the page because only it has benefits and contact."""
    posting = job_posting(soup)
    if not posting:
        return None
    offer = from_job_posting(posting)
    main = soup.find("main")
    section = main.find("section") if main else None
    if section:
        for hidden in section.select(".d-print-none"):
            hidden.decompose()
        offer["text"] = html_to_text(section)
    return offer


def empty_offer():
    return {"title": "", "company": "", "location": "", "salary": "", "posted": "", "valid_through": "", "text": ""}


def title_container(soup):
    """Largest block around the h1 that holds no site menu or footer, for pages built without main / article
    (Elementor, WordPress page builders)."""
    node = soup.find("h1")
    if not node:
        return None
    while node.parent and node.parent.name not in {"body", "html", "[document]"} \
            and not node.parent.find(["nav", "footer"]):
        node = node.parent
    return node


def generic_extract(soup):
    """Used for portals without own extractor: structured data first, then the biggest content block,
    then the block around the title."""
    posting = job_posting(soup)
    if posting and posting.get("description"):
        return from_job_posting(posting)
    candidates = soup.find_all(["main", "article"])
    content = max(candidates, key=lambda node: len(node.get_text())) if candidates else title_container(soup)
    if not content:
        return None
    offer = empty_offer()
    offer["title"] = clean(soup.find("h1")) or clean(soup.title)
    offer["text"] = html_to_text(content)
    return offer
