from core.base_scraper import BaseScraper
import requests
from bs4 import BeautifulSoup

class DuckDuckGoScraper(BaseScraper):
    handles = ['product']

    def search(self, params):
        query = params.get("query", "")
        if not query:
            return []
        url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(resp.text, "lxml")
        results = []
        for result in soup.select(".result"):
            link = result.select_one("a.result__a")
            snippet = result.select_one("a.result__snippet")
            if link:
                results.append({
                    "source": "DuckDuckGo",
                    "title": link.text.strip(),
                    "price": "",  # Not structured
                    "condition": "",
                    "vendor": "",
                    "url": link["href"],
                    "image": ""
                })
        return results
