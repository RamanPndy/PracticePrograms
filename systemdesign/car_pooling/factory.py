from systemdesign.car_pooling.models import Car, Ride, User

class RideFactory:
    @staticmethod
    def create_ride(ride_id: int, driver: User, car: Car, origin: str, destination: str, seats_available: int, price: float) -> Ride:
        return Ride(ride_id, driver, car, origin, destination, seats_available, price)
