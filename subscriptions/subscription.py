from products.product import Product
from notifications.notification import Notification
from clients.client import Client


class Subscription:
    def __init__(self, product: Product, timing: int):
        self.notifications = []
        self.product = product
        self.timing = timing

    def add_notification(self, notification: Notification) -> None:
        self.notifications.append(notification)

    def check_availability(self, client: Client):
        return self.product.check_availability(client)

    def send_notifications(self, client: Client):
        for notification in self.notifications:
            notification.notify(self.product.title,
                                self.product.content, client)
