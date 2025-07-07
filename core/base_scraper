from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def search(self, query: str) -> list:
        """
        Should return a list of dicts:
        [
            {
                'source': 'string',
                'title': 'string',
                'price': 'string',
                'condition': 'string',
                'url': 'string',
                'image': 'string or None',
            },
            ...
        ]
        """
        pass

    @property
    def name(self):
        return self.__class__.__name__
