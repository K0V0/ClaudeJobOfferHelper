"""startupjobs.cz - JobPosting data when present, otherwise the biggest content column of main."""
from common import clean, empty_offer, from_job_posting, html_to_text, job_posting

HOSTS = ("startupjobs.cz",)


def extract(soup):
    posting = job_posting(soup)
    if posting and posting.get("description"):
        return from_job_posting(posting)
    main = soup.find("main")
    columns = main.select("div.flex.flex-col.gap-6") if main else []
    if not columns:
        return None
    offer = empty_offer()
    offer["title"] = clean(main.find("h1"))
    offer["text"] = html_to_text(max(columns, key=lambda node: len(node.get_text())))
    return offer
