class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

class Car:
    def __init__(self, car_id: int, owner: User, make: str, model: str, registration_number: str):
        self.car_id = car_id
        self.owner = owner
        self.make = make
        self.model = model
        self.registration_number = registration_number

class Ride:
    def __init__(self, ride_id: int, driver: User, car: Car, origin: str, destination: str, seats_available: int, price: float):
        self.ride_id = ride_id
        self.driver = driver
        self.car = car
        self.origin = origin
        self.destination = destination
        self.seats_available = seats_available
        self.price = price
        self.passengers = []
    
    def add_passenger(self, passenger: User):
        if self.seats_available > 0:
            self.passengers.append(passenger)
            self.seats_available -= 1
        else:
            raise Exception("No seats available")

class Payment:
    def __init__(self, payment_id: int, payer: User, payee: User, amount: float):
        self.payment_id = payment_id
        self.payer = payer
        self.payee = payee
        self.amount = amount
