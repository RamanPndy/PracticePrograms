# Initialize services
from systemdesign.zoomcar.booking_manager import BookingManagerSingleton
from systemdesign.zoomcar.factory import CarFactory
from systemdesign.zoomcar.notifications import BookingNotifier
from systemdesign.zoomcar.service import CarService, UserService


car_service = CarService()
user_service = UserService()
booking_manager = BookingManagerSingleton()
notifier = BookingNotifier()

# Register observer (For demonstration purposes, assume we have a concrete observer class)
# notifier.register_observer(SomeConcreteObserver())

# Add users
user_service.add_user('user1', {'name': 'John Doe', 'email': 'john@example.com'})
user_service.add_user('user2', {'name': 'Jane Smith', 'email': 'jane@example.com'})

# Add cars
car1 = CarFactory.create_car('sedan', car_id='car1', brand='Toyota', model='Camry')
car2 = CarFactory.create_car('suv', car_id='car2', brand='Honda', model='CR-V')
car_service.add_car(car1)
car_service.add_car(car2)

# Create a booking
booking_id = booking_manager.create_booking(user_id='user1', car_id='car1', start_time='2024-07-01 10:00', end_time='2024-07-01 18:00')
notifier.notify_observers(booking_id, 'created')

# Cancel a booking
if booking_manager.cancel_booking(booking_id):
    notifier.notify_observers(booking_id, 'cancelled')
