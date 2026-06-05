import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    html = requests.get(
        url,
        timeout=15,
        headers={
            "User-Agent":"Mozilla/5.0"
        }
    ).text

    soup = BeautifulSoup(html,"html.parser")

    return soup.get_text(" ", strip=True)[:12000]