from core.base_scraper import BaseScraper
import requests
from bs4 import BeautifulSoup

class DuckDuckGoScraper(BaseScraper):
    handles = ['product']

    def search(self, params):
        query = params.get("query", "")
        if not query:
            return []
        url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(resp.text, "lxml")
            results = []
            # DuckDuckGo results are in div.result, but .result__a is the link/title
            for result in soup.select("div.result"):
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
            # Debug: If nothing was found, print the raw HTML
            if not results:
                print("DEBUG: No results found. First 500 chars of HTML:", resp.text[:500])
            return results
        except Exception as e:
            print("[DuckDuckGoScraper] Error:", e)
            return []
