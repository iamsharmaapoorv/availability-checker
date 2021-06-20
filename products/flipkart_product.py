import re
from products.online_product import OnlineProduct
from exceptions.availability_checker_exception import AvailabilityCheckerException
from clients.client import Client


class FlipkartProduct(OnlineProduct):

    def check_availability(self, client: Client):
        soup = self._parse_page()
        soup_text = soup.get_text()
        buy_now = "BUY NOW"
        text_match = re.search(
            buy_now, soup_text, re.IGNORECASE)
        if text_match:
            return True
        return False

    @property
    def title(self):
        soup = self._parse_page()
        title = soup.find("span", class_='B_NuCI')
        title_text = title.get_text().strip()
        return title_text

    @property
    def content(self):
        title = self.title
        content = title + f" is available at {self.url}"
        return content
