from abc import ABC, abstractclassmethod


class Product(ABC):
    @abstractclassmethod
    def __init__(self, url=None):
        self.url = url

    @abstractclassmethod
    def check_availability(self):
        pass

    @property
    @abstractclassmethod
    def title(self):
        pass

    @property
    @abstractclassmethod
    def content(self):
        pass
