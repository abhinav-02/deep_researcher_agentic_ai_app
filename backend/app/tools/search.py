from duckduckgo_search import DDGS

def search_web(query: str, limit: int = 5):
    urls = []

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=limit)

        for r in results:
            urls.append(r["href"])

    return urls