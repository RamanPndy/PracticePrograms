from typing import List, Optional
from datetime import datetime

class Student:
    def __init__(self, student_id: int, name: str, parent: 'Parent'):
        self.student_id = student_id
        self.name = name
        self.parent = parent
        self.pickup_time: Optional[datetime] = None
        self.drop_time: Optional[datetime] = None

class Bus:
    def __init__(self, bus_id: int, capacity: int):
        self.bus_id = bus_id
        self.capacity = capacity
        self.current_location: str = ""
        self.students_on_board: List[Student] = []

class Trip:
    def __init__(self, trip_id: int, bus: Bus):
        self.trip_id = trip_id
        self.bus = bus
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None

class Parent:
    def __init__(self, parent_id: int, name: str, email: str):
        self.parent_id = parent_id
        self.name = name
        self.email = email

class SchoolAuthority:
    def __init__(self, authority_id: int, name: str, email: str):
        self.authority_id = authority_id
        self.name = name
        self.email = email
