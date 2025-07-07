from core.base_scraper import BaseScraper

class TravelScraper(BaseScraper):
    handles = ['airfare']

    def search(self, params):
        # Placeholder for demo: would integrate Skyscanner, etc.
        return [{
            "source": "Skyscanner (demo)",
            "title": f"{params.get('from')} → {params.get('to')}, {params.get('depart_date')} ({params.get('travel_class')})",
            "price": "$500+",
            "condition": "",
            "vendor": "Various Airlines",
            "url": "",
            "image": ""
        }]
