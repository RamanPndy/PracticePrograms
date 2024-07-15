from abc import ABC, abstractmethod

from systemdesign.school_bus_tracking_system.models import Bus, Student, Trip

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

class IBusTrackerService(ABC):
    @abstractmethod
    def start_trip(self, trip: Trip):
        pass

    @abstractmethod
    def end_trip(self, trip: Trip):
        pass

    @abstractmethod
    def update_location(self, bus: Bus, location: str):
        pass

    @abstractmethod
    def onboard_student(self, bus: Bus, student: Student):
        pass

    @abstractmethod
    def offboard_student(self, bus: Bus, student: Student):
        pass
