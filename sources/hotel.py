from core.base_scraper import BaseScraper

class HotelScraper(BaseScraper):
    handles = ['hotel']

    def search(self, params):
        # Placeholder for demo: would integrate Booking.com, etc.
        return [{
            "source": "Booking.com (demo)",
            "title": f"{params.get('destination')} | {params.get('checkin')} to {params.get('checkout')} | {params.get('guests')} guest(s)",
            "price": "$100+/night",
            "condition": "",
            "vendor": "Various Hotels",
            "url": "",
            "image": ""
        }]
