from abc import ABC, abstractmethod
from typing import List

class IDeliveryManager(ABC):
    @abstractmethod
    def create_delivery(self, delivery_id: str, details: dict):
        pass

    @abstractmethod
    def assign_partner(self, delivery_id: str):
        pass

class ITripPartnerFinder(ABC):
    @abstractmethod
    def find_free_partners(self) -> List[str]:
        pass

class IPartnerAssigner(ABC):
    @abstractmethod
    def assign(self, delivery_id: str, partner_id: str):
        pass

class ITracker(ABC):
    @abstractmethod
    def start_tracking(self, partner_id: str):
        pass

    @abstractmethod
    def stop_tracking(self, partner_id: str):
        pass

    @abstractmethod
    def get_location(self, partner_id: str) -> str:
        pass
