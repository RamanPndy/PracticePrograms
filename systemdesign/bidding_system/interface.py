from abc import ABC, abstractmethod

class Bid(ABC):
    @abstractmethod
    def place_bid(self, user, amount):
        pass

    @abstractmethod
    def get_highest_bid(self):
        pass

    @abstractmethod
    def notify_users(self):
        pass

class User(ABC):
    @abstractmethod
    def update(self, message):
        pass

    @abstractmethod
    def place_bid(self, bid, amount):
        pass

