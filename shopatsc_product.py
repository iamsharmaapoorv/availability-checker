import re
from online_product import OnlineProduct
from exceptions import AvailabilityCheckerException
from client import Client


class ShopAtSCProduct(OnlineProduct):

    def check_availability(self, client: Client):
        soup = self._parse_page()
        notify_btn = soup.find(id='notify_btn_div')
        notify_btn_style = notify_btn.get('style')
        if not notify_btn_style:
            return False
        print(notify_btn, notify_btn_style)
        non_availability_text = 'display:none;'
        text_match = re.search(
            non_availability_text, notify_btn_style, re.IGNORECASE)
        print(text_match)
        if text_match:
            return True
        return False

    @property
    def title(self):
        soup = self._parse_page()
        title = soup.find("h1", class_='product-title')
        title_text = title.get_text().strip()
        return title_text

    @property
    def content(self):
        title = self.title
        content = title + f" is available at {self.url}"
        return content
