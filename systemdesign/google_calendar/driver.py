# Example usage
from datetime import datetime, timedelta
from systemdesign.google_calendar.models import Event, User
from systemdesign.google_calendar.services import AlarmService, CalendarService, NotificationService, OverlapService, SimpleOverlapStrategy


user1 = User(1, "Alice", "alice@example.com")
user2 = User(2, "Bob", "bob@example.com")

event = Event(1, "Meeting", datetime.now(), datetime.now() + timedelta(hours=1), user1, [user2])
calendar_service = CalendarService()
notification_service = NotificationService(user1)
calendar_service.register_observer(notification_service)

calendar_service.create_event(event)

# Find non-overlapping time slots
overlap_service = OverlapService(SimpleOverlapStrategy())
non_overlapping_slots = overlap_service.find_non_overlapping_slots([user1, user2], timedelta(hours=1))
print("Non-overlapping slots:", non_overlapping_slots)

# Set alarm for the event
alarm_service = AlarmService(calendar_service)
alarm_service.set_alarm(event)
