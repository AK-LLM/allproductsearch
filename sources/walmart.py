from core.base_scraper import BaseScraper
from utils.helpers import clean_price
import requests
from bs4 import BeautifulSoup

class WalmartScraper(BaseScraper):
    handles = ['product']

    def search(self, params):
        query = params.get("query", "")
        if not query:
            return []
        q = query.replace(" ", "%20")
        url = f"https://www.walmart.com/search/?query={q}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(resp.text, 'lxml')
            results = []
            for item in soup.select("div.search-result-gridview-item-wrapper, div.Grid-col"):
                title = item.select_one("a.product-title-link span, a[data-type='itemTitles']")
                price = item.select_one("span.price-characteristic")
                link = item.select_one("a.product-title-link")
                img = item.select_one("img")
                if title and price and link:
                    results.append({
                        "source": "Walmart",
                        "title": title.text.strip(),
                        "price": clean_price(price.text),
                        "condition": "new",
                        "vendor": "",
                        "url": f"https://www.walmart.com{link['href']}",
                        "image": img['src'] if img and img.has_attr('src') else ""
                    })
            return results
        except Exception as e:
            print("[WalmartScraper] Error:", e)
            return []
