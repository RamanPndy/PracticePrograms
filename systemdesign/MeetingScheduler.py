from datetime import datetime, timedelta

class Meeting:
    def __init__(self, meeting_id, title, start_time, end_time, participants):
        self.meeting_id = meeting_id
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.participants = participants
    
    def overlaps_with(self, other_meeting):
        return (self.start_time < other_meeting.end_time and self.end_time > other_meeting.start_time)

class Participant:
    def __init__(self, participant_id, name):
        self.participant_id = participant_id
        self.name = name

class MeetingScheduler:
    def __init__(self):
        self.meetings = {}

    def schedule_meeting(self, title, start_time, end_time, participants):
        meeting_id = len(self.meetings) + 1
        meeting = Meeting(meeting_id, title, start_time, end_time, participants)
        self.meetings[meeting_id] = meeting
        return meeting

    def get_meetings_for_participant(self, participant_id):
        participant_meetings = []
        for meeting in self.meetings.values():
            if any(participant.participant_id == participant_id for participant in meeting.participants):
                participant_meetings.append(meeting)
        return participant_meetings

    def get_available_time_slots(self, participant_id, duration, start_date, end_date):
        available_slots = []
        current_date = start_date
        while current_date <= end_date:
            start_time = current_date
            end_time = current_date + timedelta(minutes=duration)
            if not any(self.is_overlap(start_time, end_time, meeting.start_time, meeting.end_time) 
                       for meeting in self.get_meetings_for_participant(participant_id)):
                available_slots.append((start_time, end_time))
            current_date += timedelta(days=1)
        return available_slots

    def is_overlap(self, start_time1, end_time1, start_time2, end_time2):
        return start_time1 < end_time2 and end_time1 > start_time2
    
    def has_conflict(self, new_meeting):
        for meeting in self.meetings.values():
            if new_meeting.overlaps_with(meeting):
                return True
        return False
    
    def cancel_meeting(self, meeting_id):
        if meeting_id in self.meetings:
            del self.meetings[meeting_id]
            return True
        else:
            return False
    
    def is_available(self, start_time, end_time):
        for meeting in self.meetings.values():
            if (meeting.start_time <= start_time < meeting.end_time) or \
               (meeting.start_time < end_time <= meeting.end_time) or \
               (start_time <= meeting.start_time and end_time >= meeting.end_time):
                return False
        return True

    def get_meeting(self, meeting_id):
        return self.meetings.get(meeting_id)

# Example usage
if __name__ == "__main__":
    scheduler = MeetingScheduler()

    # Schedule meetings
    participant1 = Participant(1, "Alice")
    participant2 = Participant(2, "Bob")
    meeting1 = scheduler.schedule_meeting("Project Review", datetime(2024, 2, 10, 10, 0), datetime(2024, 2, 10, 11, 0), [participant1, participant2])
    meeting2 = scheduler.schedule_meeting("Team Sync", datetime(2024, 2, 12, 14, 0), datetime(2024, 2, 12, 15, 0), [participant1])

    # Get meetings for a participant
    print("Meetings for Alice:")
    for meeting in scheduler.get_meetings_for_participant(1):
        print(meeting.title)

    # Get available time slots for a participant
    print("Available time slots for Alice:")
    for start_time, end_time in scheduler.get_available_time_slots(1, 30, datetime(2024, 2, 10), datetime(2024, 2, 14)):
        print(f"{start_time} - {end_time}")
