from core.base_scraper import BaseScraper
from utils.helpers import clean_price
import requests
from bs4 import BeautifulSoup

class GoogleShoppingScraper(BaseScraper):
    handles = ['product']

    def search(self, params):
        query = params.get("query", "")
        if not query:
            return []
        q = query.replace(" ", "+")
        url = f"https://www.google.com/search?tbm=shop&q={q}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        try:
            r = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(r.text, "lxml")
            results = []
            for item in soup.select("div.sh-dgr__content"):
                title = item.select_one("h4.tAxDx")
                price = item.select_one(".a8Pemb")
                vendor = item.select_one(".aULzUe")
                link = item.select_one("a.shntl")
                image = item.select_one("img")
                if title and price and vendor and link:
                    results.append({
                        "source": "GoogleShopping",
                        "title": title.text.strip(),
                        "price": clean_price(price.text),
                        "condition": "",
                        "vendor": vendor.text.strip(),
                        "url": "https://www.google.com" + link["href"],
                        "image": image["src"] if image and image.has_attr("src") else ""
                    })
            return results
        except Exception as e:
            print("[GoogleShoppingScraper] Error:", e)
            return []
