from systemdesign.zoomcar.interface import Booking


class BookingManagerSingleton(Booking):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(BookingManagerSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.bookings = {}

    def create_booking(self, user_id: str, car_id: str, start_time: str, end_time: str) -> str:
        booking_id = f"{user_id}-{car_id}-{start_time}"
        self.bookings[booking_id] = {
            'user_id': user_id,
            'car_id': car_id,
            'start_time': start_time,
            'end_time': end_time
        }
        return booking_id

    def cancel_booking(self, booking_id: str) -> bool:
        if booking_id in self.bookings:
            del self.bookings[booking_id]
            return True
        return False
