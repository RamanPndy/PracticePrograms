from abc import ABC, abstractmethod
from systemdesign.logistic_system.models import Container, Location

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
    def notify_observers(self):
        pass

class ITrackingService(ABC):
    @abstractmethod
    def get_realtime_location(self, container: Container) -> Location:
        pass
