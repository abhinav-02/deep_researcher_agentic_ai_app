from ddgs import DDGS
from urllib.parse import urlparse


BLOCKED_PATH_KEYWORDS = [
    "/search",
    "/login",
    "/signup",
    "wikipedia.org/wiki/Research",
    "dictionary",
]


def is_bad_url(url: str) -> bool:
    u = url.lower()

    return any(x in u for x in BLOCKED_PATH_KEYWORDS)


def is_landing_page(url: str) -> bool:
    """
    Filters out pages that are NOT content-heavy articles
    """
    parsed = urlparse(url)

    path = parsed.path.lower()

    # very short paths like /, /wiki/, /search
    if path in ["", "/", "/wiki"]:
        return True

    if len(path.split("/")) < 2:
        return True

    return False


def search_web(query: str, max_results: int = 8):

    # generic query expansion (NOT domain-specific)
    refined_query = f"{query} explanation guide overview details"

    urls = []

    with DDGS() as ddgs:
        results = ddgs.text(
            refined_query,
            max_results=20
        )

        for r in results:
            url = r.get("href")

            if not url:
                continue

            url = url.split("?")[0]

            # filter junk
            if is_bad_url(url):
                continue

            # avoid pure navigation pages
            if is_landing_page(url):
                continue

            urls.append(url)

    # remove duplicates while preserving order
    seen = set()
    cleaned = []

    for u in urls:
        if u not in seen:
            cleaned.append(u)
            seen.add(u)

    return cleaned[:max_results]

