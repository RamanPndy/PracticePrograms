from datetime import datetime
from typing import List
from systemdesign.school_bus_tracking_system.interface import IBusTrackerService, IObserver, ISubject
from systemdesign.school_bus_tracking_system.models import Bus, Parent, Student, Trip

class BusTrackerService(ISubject, IBusTrackerService):
    def __init__(self):
        self.observers: List[IObserver] = []
        self.trips: List[Trip] = []

    def register_observer(self, observer: IObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: IObserver):
        self.observers.remove(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)

    def start_trip(self, trip: Trip):
        trip.start_time = datetime.now()
        self.trips.append(trip)
        self.notify_observers(f"Trip {trip.trip_id} has started.")

    def end_trip(self, trip: Trip):
        trip.end_time = datetime.now()
        self.notify_observers(f"Trip {trip.trip_id} has ended.")

    def update_location(self, bus: Bus, location: str):
        bus.current_location = location
        self.notify_observers(f"Bus {bus.bus_id} is now at {location}.")

    def onboard_student(self, bus: Bus, student: Student):
        bus.students_on_board.append(student)
        student.pickup_time = datetime.now()
        self.notify_observers(f"Student {student.name} has boarded Bus {bus.bus_id}.")

    def offboard_student(self, bus: Bus, student: Student):
        bus.students_on_board.remove(student)
        student.drop_time = datetime.now()
        self.notify_observers(f"Student {student.name} has alighted from Bus {bus.bus_id}.")

class NotificationService(IObserver):
    def __init__(self, parent: Parent):
        self.parent = parent

    def update(self, message: str):
        self.send_notification(message)

    def send_notification(self, message: str):
        print(f"Notification to {self.parent.name}: {message}")
