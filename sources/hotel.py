from core.base_scraper import BaseScraper

class HotelScraper(BaseScraper):
    handles = ['hotel']

    def search(self, params):
        # Placeholder: You would implement Booking.com/Agoda API or scraping here
        # Return a mock result for demo
        return [{
            "source": "Booking.com (demo)",
            "title": f"{params.get('destination')} | {params.get('checkin')} to {params.get('checkout')} | {params.get('guests')} guest(s)",
            "price": "$100+/night",
            "condition": "",
            "vendor": "Various Hotels",
            "url": "",
            "image": ""
        }]
