from core.base_scraper import BaseScraper
from duckduckgo_search import DDGS

class WebSearchScraper(BaseScraper):
    """
    Fallback: Uses DuckDuckGo to find product URLs, tries to extract titles and (if possible) price.
    """
    def search(self, query):
        # DuckDuckGo limits, but is lightweight and doesn't require API keys
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=20):
                results.append({
                    "source": "DuckDuckGo",
                    "title": r['title'],
                    "price": "",  # No price; just a URL, user can follow
                    "condition": "",
                    "url": r['href'],
                    "image": "",
                })
        return results
