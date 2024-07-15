from abc import ABC, abstractmethod
from typing import List

from systemdesign.log_tracking_system.models import Log

class IObserver(ABC):
    @abstractmethod
    def update(self, log: Log):
        pass

class ISubject(ABC):
    @abstractmethod
    def register_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def notify_observers(self, log: Log):
        pass

class ILogFilterStrategy(ABC):
    @abstractmethod
    def filter(self, logs: List[Log]) -> List[Log]:
        pass

class ILogSearchStrategy(ABC):
    @abstractmethod
    def search(self, logs: List[Log], query: str) -> List[Log]:
        pass
