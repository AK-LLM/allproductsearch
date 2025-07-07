from core.base_scraper import BaseScraper
from utils.helpers import clean_price
import requests
from bs4 import BeautifulSoup

class EbayScraper(BaseScraper):
    handles = ['product']

    def search(self, params):
        query = params.get("query", "")
        if not query:
            return []
        q = query.replace(" ", "+")
        url = f"https://www.ebay.com/sch/i.html?_nkw={q}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(resp.text, 'lxml')
            results = []
            for item in soup.select(".s-item"):
                title = item.select_one(".s-item__title")
                price = item.select_one(".s-item__price")
                link = item.select_one(".s-item__link")
                img = item.select_one(".s-item__image-img")
                cond = item.select_one(".SECONDARY_INFO")
                if title and price and link:
                    results.append({
                        "source": "eBay",
                        "title": title.text.strip(),
                        "price": clean_price(price.text),
                        "condition": cond.text.strip() if cond else "",
                        "vendor": "",
                        "url": link['href'],
                        "image": img['src'] if img and img.has_attr('src') else ""
                    })
            return results
        except Exception as e:
            print("[EbayScraper] Error:", e)
            return []
