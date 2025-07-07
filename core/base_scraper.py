from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def search(self, params: dict) -> list:
        """
        Returns list of dicts, each dict representing a result.
        """
        pass

    @property
    def name(self):
        return self.__class__.__name__
