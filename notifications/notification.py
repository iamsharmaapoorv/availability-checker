from abc import ABC, abstractclassmethod
from clients.client import Client


class Notification(ABC):

    @staticmethod
    @abstractclassmethod
    def notify(title: str, content: str, client: Client) -> None:
        pass

    @staticmethod
    def get_content(title: str, url: str) -> str:
        content = f"{title} is available right now at {url}."
        return content
