from abc import ABC, abstractmethod


class BookingObserver(ABC):
    @abstractmethod
    def update(self, booking_id: str, status: str) -> None:
        pass

class BookingNotifier:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer: BookingObserver):
        self.observers.append(observer)

    def unregister_observer(self, observer: BookingObserver):
        self.observers.remove(observer)

    def notify_observers(self, booking_id: str, status: str):
        for observer in self.observers:
            observer.update(booking_id, status)
