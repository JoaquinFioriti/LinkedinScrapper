from abc import ABC, abstractmethod


class Scrapper(ABC):

    @abstractmethod
    def scrape(self, driver, url):
        pass
