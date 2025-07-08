from core.base_scraper import BaseScraper
import requests
from bs4 import BeautifulSoup

class DuckDuckGoScraper(BaseScraper):
    handles = ['product']

    def search(self, params):
        print("DuckDuckGoScraper: search() called", flush=True)  # Debug line
        query = params.get("query", "")
        if not query:
            print("DEBUG: No query provided.", flush=True)
            return []
        url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            html = resp.text
            soup = BeautifulSoup(html, "lxml")
            results = []
            for result in soup.select("div.web-result, div.result"):
                link = result.select_one("a.result__a")
                if link:
                    results.append({
                        "source": "DuckDuckGo",
                        "title": link.text.strip(),
                        "price": "",
                        "condition": "",
                        "vendor": "",
                        "url": link["href"],
                        "image": ""
                    })
            if not results:
                print("DEBUG: NO RESULTS. HTML START:", flush=True)
                print(html[:1000], flush=True)
            else:
                print(f"DEBUG: {len(results)} DuckDuckGo results found.", flush=True)
            return results
        except Exception as e:
            print("[DuckDuckGoScraper] Error:", e, flush=True)
            return []
