import time
from random import random
from datetime import datetime, timedelta
from exceptions import AvailabilityCheckerException
from subscription import Subscription
from heapq import *


class Profile:
    def __init__(self, client):
        self.client = client
        self.subscriptions = set()
        # self.notifications = []
        self.subscription_queue = []

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            raise AvailabilityCheckerException(
                "Already following this subscription.")

        self.subscriptions.add(subscription)
        heappush(self.subscription_queue,
                 (datetime.now(), random(), subscription))

    def check_availability(self):
        if not self.subscription_queue:
            return
        while datetime.now() >= self.subscription_queue[0][0]:
            current = heappop(self.subscription_queue)
            next_check_timing = datetime.now(
            )+timedelta(minutes=current[2].timing)
            heappush(self.subscription_queue,
                     (next_check_timing, random(), current[2]))
            if current[2].check_availability(self.client):
                current[2].send_notifications(self.client)

    def ping(self):
        while(True):
            self.check_availability()
            time.sleep(15)
