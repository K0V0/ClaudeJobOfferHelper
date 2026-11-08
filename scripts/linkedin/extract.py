"""linkedin.com - public page has JobPosting data, the HTML description is the fallback. Rate limits quickly (HTTP 429)."""
from common import clean, empty_offer, from_job_posting, html_to_text, job_posting

HOSTS = ("linkedin.com",)


def extract(soup):
    posting = job_posting(soup)
    markup = soup.select_one(".show-more-less-html__markup")
    if posting and posting.get("description"):
        offer = from_job_posting(posting)
    elif markup:
        offer = empty_offer()
        offer["title"] = clean(soup.select_one(".top-card-layout__title")) or clean(soup.find("h1"))
        offer["company"] = clean(soup.select_one(".topcard__org-name-link"))
        offer["location"] = clean(soup.select_one(".topcard__flavor--bullet"))
        offer["text"] = html_to_text(markup)
    else:
        return None
    criteria = [clean(node) for node in soup.select(".description__job-criteria-item")]
    if criteria:
        offer["text"] += "\n\n## Job criteria\n\n" + "\n".join(f"- {item}" for item in criteria)
    return offer
