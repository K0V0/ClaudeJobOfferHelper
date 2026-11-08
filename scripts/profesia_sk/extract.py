"""profesia.sk - offer text is in main#detail .card-content, facts like salary in the .overall-info block inside it."""
from common import clean, empty_offer, html_to_text

HOSTS = ("profesia.sk",)


def _facts(info):
    parts = [part.strip() for part in info.get_text("|", strip=True).split("|")]
    facts = {}
    label = None
    for part in parts:
        if part.endswith(":"):
            label = part[:-1]
            facts[label] = ""
        elif label:
            facts[label] = f"{facts[label]} {part}".strip()
    return facts


def extract(soup):
    main = soup.select_one("main#detail")
    card = main.select_one(".card-content") if main else None
    if not card:
        return None
    offer = empty_offer()
    offer["title"] = clean(main.find("h1")) or clean(soup.find("h1"))
    posted = soup.select_one('[itemprop="datePosted"]')
    offer["posted"] = (posted.get("content", "") or clean(posted))[:10] if posted else ""
    info = card.select_one(".overall-info")
    facts = _facts(info) if info else {}
    offer["company"] = facts.get("Spoločnosť", "")
    offer["location"] = facts.get("lokalita", "")
    offer["salary"] = facts.get("Základná zložka mzdy (brutto)", "")
    for noise in card.select(".button-bar, .btn-group, .overall-info, a.btn"):
        noise.decompose()
    sections = [html_to_text(card)]
    if facts:
        sections.append("## Informácie o ponuke\n\n" + "\n".join(f"- {name}: {value}" for name, value in facts.items()))
    offer["text"] = "\n\n".join(sections)
    return offer
