from core.base_scraper import BaseScraper
from utils.helpers import clean_price
import requests
from bs4 import BeautifulSoup

class MarketplaceScraper(BaseScraper):
    """
    Example: Scrapes eBay results. You can add others in here as well.
    """
    def search(self, query):
        query_str = query.replace("+", " ").replace(" ", "+")
        url = f"https://www.ebay.com/sch/i.html?_nkw={query_str}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers)
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
                    "url": link['href'],
                    "image": img['src'] if img and img.has_attr('src') else None,
                })
        # Add more marketplaces (Kijiji, OfferUp, etc.) using similar logic
        return results
