
from systemdesign.bidding_system.interface import Bid, User

class AuctionBid(Bid):
    def __init__(self):
        self.bids = {}
        self.users = []

    def place_bid(self, user, amount):
        self.bids[user] = amount
        if user not in self.users:
            self.users.append(user)
        self.notify_users()

    def get_highest_bid(self):
        if not self.bids:
            return None
        return max(self.bids.items(), key=lambda x: x[1])

    def notify_users(self):
        highest_bidder, highest_bid = self.get_highest_bid()
        for user in self.users:
            user.update(f"New highest bid: {highest_bid} by {highest_bidder.name}")

class AuctionUser(User):
    def __init__(self, name):
        self.name = name
        self.notifications = []

    def update(self, message):
        self.notifications.append(message)
        print(f"Notification for {self.name}: {message}")

    def place_bid(self, bid, amount):
        bid.place_bid(self, amount)


