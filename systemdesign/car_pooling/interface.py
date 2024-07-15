from abc import ABC, abstractmethod

class IUser(ABC):
    @abstractmethod
    def register_user(self, user_details: dict):
        pass

    @abstractmethod
    def search_rides(self, origin: str, destination: str):
        pass

    @abstractmethod
    def book_ride(self, ride_id: int):
        pass

    @abstractmethod
    def offer_ride(self, ride_details: dict):
        pass

class ICar(ABC):
    @abstractmethod
    def register_car(self, car_details: dict):
        pass

class IRide(ABC):
    @abstractmethod
    def create_ride(self, ride_details: dict):
        pass

    @abstractmethod
    def cancel_ride(self, ride_id: int):
        pass

    @abstractmethod
    def get_ride_details(self, ride_id: int):
        pass

class IPayment(ABC):
    @abstractmethod
    def make_payment(self, payment_details: dict):
        pass

    @abstractmethod
    def receive_payment(self, payment_details: dict):
        pass
