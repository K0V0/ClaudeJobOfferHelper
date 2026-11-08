"""prace.cz - see from_alma_page."""
from common import from_alma_page

HOSTS = ("prace.cz",)


def extract(soup):
    return from_alma_page(soup)
