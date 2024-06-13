from datetime import datetime

class Deal:
    def __init__(self, deal_id: int, item_id: int, price: float, quantity: int, end_time: datetime):
        self.deal_id = deal_id
        self.item_id = item_id
        self.price = price
        self.quantity = quantity
        self.end_time = end_time
        self.claimed_users = set()

    def is_active(self) -> bool:
        return datetime.now() < self.end_time and self.quantity > 0

    def claim(self, user_id: int) -> bool:
        if not self.is_active() or user_id in self.claimed_users:
            return False
        self.quantity -= 1
        self.claimed_users.add(user_id)
        return True
