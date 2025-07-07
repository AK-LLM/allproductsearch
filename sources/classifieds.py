from core.base_scraper import BaseScraper
from utils.helpers import clean_price
import requests
from bs4 import BeautifulSoup

class ClassifiedsScraper(BaseScraper):
    """
    Example: Scrapes Craigslist as a demo.
    """
    def search(self, query):
        # Using the Vancouver Craigslist as an example; you may want to geolocate or rotate cities
        query_str = query.replace("+", " ").replace(" ", "+")
        url = f"https://vancouver.craigslist.org/search/sss?query={query_str}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        results = []
        for row in soup.select("li.result-row"):
            title = row.select_one(".result-title")
            price = row.select_one(".result-price")
            link = title['href'] if title else None
            img = row.select_one(".result-image img")
            if title and price and link:
                results.append({
                    "source": "Craigslist",
                    "title": title.text.strip(),
                    "price": clean_price(price.text),
                    "condition": "used",  # Assume used for classifieds
                    "url": link,
                    "image": img['src'] if img and img.has_attr('src') else None,
                })
        return results
