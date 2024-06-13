from interface import DealInterface
from models import Deal
from datetime import datetime, timedelta

class DealManager(DealInterface):
    _instance = None
    deals = {}
    next_deal_id = 1

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DealManager, cls).__new__(cls)
        return cls._instance

    def create_deal(self, item_id: int, price: float, quantity: int, duration: int) -> None:
        deal_id = self.next_deal_id
        self.next_deal_id += 1
        end_time = datetime.now() + timedelta(hours=duration)
        deal = Deal(deal_id, item_id, price, quantity, end_time)
        self.deals[deal_id] = deal

    def end_deal(self, deal_id: int) -> None:
        if deal_id in self.deals:
            self.deals[deal_id].end_time = datetime.now()

    def update_deal(self, deal_id: int, quantity: int = None, duration: int = None) -> None:
        if deal_id in self.deals:
            if quantity is not None:
                self.deals[deal_id].quantity = quantity
            if duration is not None:
                self.deals[deal_id].end_time = datetime.now() + timedelta(hours=duration)

    def claim_deal(self, user_id: int, deal_id: int) -> bool:
        if deal_id in self.deals:
            return self.deals[deal_id].claim(user_id)
        return False
