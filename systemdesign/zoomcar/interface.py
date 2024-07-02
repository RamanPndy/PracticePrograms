from abc import ABC, abstractmethod
from typing import List, Dict

class Car(ABC):
    @abstractmethod
    def get_details(self) -> Dict[str, str]:
        pass

class Booking(ABC):
    @abstractmethod
    def create_booking(self, user_id: str, car_id: str, start_time: str, end_time: str) -> str:
        pass

    @abstractmethod
    def cancel_booking(self, booking_id: str) -> bool:
        pass

class User(ABC):
    @abstractmethod
    def get_profile(self, user_id: str) -> Dict[str, str]:
        pass
