import requests
from products.product import Product
from products.headers import DEFAULT_HEADERS
from bs4 import BeautifulSoup


class OnlineProduct(Product):
    def __init__(self, url=None, in_stock_text=None):
        self.url = url  # call super?
        self.in_stock_text = in_stock_text

    def _parse_page(self):
        # with open('headers.json') as header_file:
        # headers = header_file.json()

        get_request = requests.get(self.url, headers=DEFAULT_HEADERS)
        soup = BeautifulSoup(get_request.text, "html.parser")
        return soup
