import trafilatura

def scrape_url(url):
    try:
        downloaded = trafilatura.fetch_url(url)

        if not downloaded:
            return ""

        text = trafilatura.extract(downloaded)

        return text or ""

    except Exception:
        return ""