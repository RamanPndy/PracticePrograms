# Example usage
from systemdesign.school_bus_tracking_system.models import Bus, Parent, Student, Trip
from systemdesign.school_bus_tracking_system.services import BusTrackerService, NotificationService

parent = Parent(1, "Alice", "alice@example.com")
student = Student(1, "Bob", parent)
bus = Bus(1, 50)
trip = Trip(1, bus)

bus_tracker_service = BusTrackerService()
notification_service = NotificationService(parent)
bus_tracker_service.register_observer(notification_service)

bus_tracker_service.start_trip(trip)
bus_tracker_service.onboard_student(bus, student)
bus_tracker_service.update_location(bus, "123 Main St")
bus_tracker_service.offboard_student(bus, student)
bus_tracker_service.end_trip(trip)