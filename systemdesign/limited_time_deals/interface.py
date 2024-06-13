from abc import ABC, abstractmethod

class DealInterface(ABC):
    @abstractmethod
    def create_deal(self, item_id: int, price: float, quantity: int, duration: int) -> None:
        pass

    @abstractmethod
    def end_deal(self, deal_id: int) -> None:
        pass

    @abstractmethod
    def update_deal(self, deal_id: int, quantity: int = None, duration: int = None) -> None:
        pass

    @abstractmethod
    def claim_deal(self, user_id: int, deal_id: int) -> bool:
        pass
