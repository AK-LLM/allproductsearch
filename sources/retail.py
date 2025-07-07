from core.base_scraper import BaseScraper
from utils.helpers import clean_price
import requests
from bs4 import BeautifulSoup

class RetailScraper(BaseScraper):
    """
    Example: Scrapes Walmart search results as a demo.
    Add more retailers inside this class or as methods.
    """
    def search(self, query):
        query_str = query.replace("+", " ").replace(" ", "%20")
        url = f"https://www.walmart.com/search?q={query_str}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        results = []
        for item in soup.select("div.search-result-gridview-item"):
            title = item.select_one("a.product-title-link span")
            price = item.select_one("span.price-main span.visuallyhidden")
            link = item.select_one("a.product-title-link")
            img = item.select_one("img")
            if title and price and link:
                results.append({
                    "source": "Walmart",
                    "title": title.text.strip(),
                    "price": clean_price(price.text),
                    "condition": "new",
                    "url": f"https://www.walmart.com{link['href']}",
                    "image": img['src'] if img and img.has_attr('src') else None,
                })
        # You can add more retail sites here (BestBuy, Newegg, etc.) with similar logic
        return results
