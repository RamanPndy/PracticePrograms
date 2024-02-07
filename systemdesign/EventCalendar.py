from datetime import datetime, timedelta
import uuid

class Event:
    def __init__(self, title, start_time, end_time):
        self.id = str(uuid.uuid4())
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, title, start_time, end_time):
        event = Event(title, start_time, end_time)
        self.events.append(event)
        print(f"Event '{title}' added to the calendar.")

    def update_event(self, event_id, title=None, start_time=None, end_time=None):
        event = self.get_event_by_id(event_id)
        if event:
            if title:
                event.title = title
            if start_time:
                event.start_time = start_time
            if end_time:
                event.end_time = end_time
            print(f"Event '{event.title}' updated successfully.")
        else:
            print("Event not found.")

    def delete_event(self, event_id):
        event = self.get_event_by_id(event_id)
        if event:
            self.events.remove(event)
            print("Event deleted successfully.")
        else:
            print("Event not found.")

    def get_event_by_id(self, event_id):
        for event in self.events:
            if event.id == event_id:
                return event
        return None

    def get_events_in_range(self, start_time, end_time):
        events_in_range = []
        for event in self.events:
            if event.start_time >= start_time and event.end_time <= end_time:
                events_in_range.append(event)
        return events_in_range

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.calendar = Calendar()

    def add_event_to_calendar(self, event):
        self.calendar.add_event(event)

# Example usage
if __name__ == "__main__":
    calendar = Calendar()

    # Add events
    calendar.add_event("Meeting", datetime(2024, 2, 10, 10, 0), datetime(2024, 2, 10, 11, 0))
    calendar.add_event("Lunch", datetime(2024, 2, 11, 12, 0), datetime(2024, 2, 11, 13, 0))
    calendar.add_event("Presentation", datetime(2024, 2, 12, 14, 0), datetime(2024, 2, 12, 15, 0))

    # Update event
    calendar.update_event(calendar.events[0].id, title="Updated Meeting")

    # Delete event
    calendar.delete_event(calendar.events[1].id)

    # Get events in range
    start_time = datetime(2024, 2, 10)
    end_time = datetime(2024, 2, 12)
    events_in_range = calendar.get_events_in_range(start_time, end_time)
    print("Events in range:")
