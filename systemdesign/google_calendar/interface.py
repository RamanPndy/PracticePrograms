from abc import ABC, abstractmethod
from datetime import timedelta
from typing import List

from systemdesign.google_calendar.models import TimeSlot, User

class IObserver(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class ISubject(ABC):
    @abstractmethod
    def register_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def notify_observers(self, message: str):
        pass

class IOverlapStrategy(ABC):
    @abstractmethod
    def find_non_overlapping_slots(self, users: List[User], duration: timedelta) -> List[TimeSlot]:
        pass
