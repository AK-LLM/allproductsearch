from core.base_scraper import BaseScraper
import requests
from bs4 import BeautifulSoup

class BingScraper(BaseScraper):
    handles = ['product']

    def search(self, params):
        print("BingScraper: search() called", flush=True)
        query = params.get("query", "")
        if not query:
            print("DEBUG: No query provided.", flush=True)
            return []
        url = f"https://www.bing.com/search?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            html = resp.text
            soup = BeautifulSoup(html, "lxml")
            results = []
            for li in soup.select("li.b_algo"):
                a = li.find("a")
                if not a: continue
                title = a.text.strip()
                url = a["href"]
                snippet = li.find("p")
                results.append({
                    "source": "Bing",
                    "title": title,
                    "price": "",  # Not structured
                    "condition": "",
                    "vendor": "",
                    "url": url,
                    "image": ""
                })
            if not results:
                print("DEBUG: NO RESULTS. HTML START:", flush=True)
                print(html[:1000], flush=True)
            else:
                print(f"DEBUG: {len(results)} Bing results found.", flush=True)
            return results
        except Exception as e:
            print("[BingScraper] Error:", e, flush=True)
            return []
