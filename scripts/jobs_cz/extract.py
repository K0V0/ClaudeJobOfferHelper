"""jobs.cz - three layouts: data-test attributes, company branded article.cp-detail (needs JavaScript), new beta.jobs.cz."""
import re

from common import clean, empty_offer, from_alma_page, html_to_text

HOSTS = ("jobs.cz",)


def _labelled(soup, label):
    for item in soup.select('[data-test="jd-info-item"]'):
        text = clean(item)
        if text.startswith(label):
            return text[len(label):].strip()
    return ""


def _standard(soup, body):
    offer = empty_offer()
    offer["title"] = clean(soup.find("h1"))
    offer["company"] = _labelled(soup, "Společnost")
    offer["location"] = clean(soup.select_one('[data-test="jd-info-location"]'))
    offer["salary"] = re.sub(r"^Plat\s*", "", clean(soup.select_one('[data-test="jd-salary"]')))
    sections = [html_to_text(node) for node in soup.select('[data-test="jd-header-text"]')]
    sections.append(html_to_text(body))
    benefits = [clean(node) for node in soup.select('[data-test="jd-benefits"]')]
    if benefits:
        sections.append("## Benefity\n\n" + "\n".join(f"- {benefit}" for benefit in benefits))
    details = [clean(node) for node in soup.select('[data-test="jd-info-item"]')]
    if details:
        sections.append("## Informace o pozici\n\n" + "\n".join(f"- {detail}" for detail in details))
    offer["text"] = "\n\n".join(section for section in sections if section)
    return offer


def _branded_company(page_title, job_title):
    """Page title of a branded offer is `<job> | <company>` or `<job> - <company>`."""
    if "|" in page_title:
        return page_title.rpartition("|")[2].strip()
    return page_title[len(job_title):].strip(" -") if page_title.startswith(job_title) else ""


def extract(soup):
    body = soup.select_one('[data-test="jd-body-richtext"]')
    if body:
        return _standard(soup, body)
    branded = soup.select_one("article.cp-detail")
    if not branded:
        return from_alma_page(soup)
    offer = empty_offer()
    offer["title"] = clean(branded.find("h1")) or clean(soup.find("h1"))
    offer["company"] = _branded_company(clean(soup.title), offer["title"])
    offer["text"] = html_to_text(branded)
    return offer
