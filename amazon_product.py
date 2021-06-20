import re
from online_product import OnlineProduct
from exceptions import AvailabilityCheckerException
from client import Client


class AmazonProduct(OnlineProduct):
    def __init__(self, url, in_stock_text="In stock."):
        super().__init__(url)
        self.in_stock_text = in_stock_text

    def check_availability(self, client: Client):
        soup = self._parse_page()
        availability_soup = soup.find(id='availability')
        soup_list = list(availability_soup)
        if not self.in_stock_text:
            raise AvailabilityCheckerException(
                "Stock availability text to match with is unavailable.")

        text_match = re.search(
            self.in_stock_text, soup_list[1].get_text(), re.IGNORECASE)
        if text_match:
            return True
        return False

    @property
    def title(self):
        soup = self._parse_page()
        title = soup.find(id='productTitle')
        title_text = title.get_text().strip()
        return title_text

    @property
    def content(self):
        title = self.title
        content = title + f" is available at {self.url}"
        return content
