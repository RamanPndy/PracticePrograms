from datetime import datetime, timedelta
from typing import List
from systemdesign.google_calendar.interface import IObserver, IOverlapStrategy, ISubject
from systemdesign.google_calendar.models import Event, TimeSlot, User

class CalendarService(ISubject):
    def __init__(self):
        self.observers: List[IObserver] = []
        self.events: List[Event] = []

    def register_observer(self, observer: IObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: IObserver):
        self.observers.remove(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)

    def create_event(self, event: Event):
        self.events.append(event)
        self.notify_observers(f"New event created: {event.title}")

    def modify_event(self, event_id: int, new_event: Event):
        for event in self.events:
            if event.event_id == event_id and event.creator == new_event.creator:
                event.title = new_event.title
                event.start_time = new_event.start_time
                event.end_time = new_event.end_time
                event.participants = new_event.participants
                self.notify_observers(f"Event modified: {event.title}")
                return True
        return False

    def add_participant(self, event_id: int, participant: User):
        for event in self.events:
            if event.event_id == event_id and event.creator == participant:
                event.participants.append(participant)
                self.notify_observers(f"New participant added: {participant.name} to event {event.title}")
                return True
        return False

class NotificationService(IObserver):
    def __init__(self, user: User):
        self.user = user

    def update(self, message: str):
        self.send_notification(message)

    def send_notification(self, message: str):
        print(f"Notification to {self.user.name}: {message}")

class AlarmService:
    def __init__(self, calendar_service: CalendarService):
        self.calendar_service = calendar_service

    def set_alarm(self, event: Event):
        alarm_time = event.start_time - timedelta(minutes=10)
        print(f"Alarm set for event {event.title} at {alarm_time}")

class OverlapService:
    def __init__(self, strategy: IOverlapStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: IOverlapStrategy):
        self.strategy = strategy

    def find_non_overlapping_slots(self, users: List[User], duration: timedelta) -> List[TimeSlot]:
        return self.strategy.find_non_overlapping_slots(users, duration)

class SimpleOverlapStrategy(IOverlapStrategy):
    def find_non_overlapping_slots(self, users: List[User], duration: timedelta) -> List[TimeSlot]:
        # Implement a simple strategy to find non-overlapping slots
        available_slots = []
        # This is a placeholder implementation
        # Actual implementation would involve checking users' schedules
        start_time = datetime.now()
        end_time = start_time + duration
        available_slots.append(TimeSlot(start_time, end_time))
        return available_slots
