from datetime import datetime, timedelta
from typing import List, Optional

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.events: List[Event] = []

    def add_event(self, event: 'Event'):
        self.events.append(event)

class Event:
    def __init__(self, event_id: int, title: str, start_time: datetime, end_time: datetime, creator: User, participants: List[User]):
        self.event_id = event_id
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.creator = creator
        self.participants = participants

class Notification:
    def __init__(self, message: str, recipient: User, timestamp: datetime):
        self.message = message
        self.recipient = recipient
        self.timestamp = timestamp

class TimeSlot:
    def __init__(self, start_time: datetime, end_time: datetime):
        self.start_time = start_time
        self.end_time = end_time
