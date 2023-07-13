from enum import Enum
from abc import ABC
from datetime import datetime

class BillItemType(Enum):
    BASE_CHARGE, ADDITIONAL_SERVICE, FINE, OTHER = 1, 2, 3, 4

class VehicleLogType(Enum):
    ACCIDENT, FUELING, CLEANING_SERVICE, OIL_CHANGE, REPAIR, OTHER = 1, 2, 3, 4, 5, 6

class VanType(Enum):
    PASSENGER, CARGO = 1, 2

class CarType(Enum):
    ECONOMY, COMPACT, INTERMEDIATE, STANDARD, FULL_SIZE, PREMIUM, LUXURY = 1, 2, 3, 4, 5, 6, 7

class VehicleStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST, BEING_SERVICED, OTHER = 1, 2, 3, 4, 5, 6

class ReservationStatus(Enum):
    ACTIVE, PENDING, CONFIRMED, COMPLETED, CANCELLED, NONE = 1, 2, 3, 4, 5, 6

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5

class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

class Person():
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone

class Account(ABC):
    def __init__(self, id, password, person, status=AccountStatus.NONE):
        self.__id = id
        self.__password = password
        self.__status = AccountStatus.NONE
        self.__person = person

    def reset_password(self):
        None

class Member(Account):
    def __init__(self):
        self.__total_vehicles_reserved = 0

    def get_reservations(self):
        None

class Receptionist(Account):
    def __init__(self, date_joined):
        self.__date_joined = date_joined

    def search_member(self, name):
        None

class AdditionalDriver:
    def __init__(self, id, person):
        self.__driver_id = id
        self.__person = person

class CarRentalLocation:
    def __init__(self, name, address):
        self.__name = name
        self.__location = address

    def get_location(self):
        return self.__location

class CarRentalSystem:
    def __init__(self, name):
        self.__name = name
        self.__locations = []

    def add_new_location(self, location):
        None

class Vehicle(ABC):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof, status, model, make, manufacturing_year,
                 mileage):
        self.__license_number = license_num
        self.__stock_number = stock_num
        self.__passenger_capacity = capacity
        self.__barcode = barcode
        self.__has_sunroof = has_sunroof
        self.__status = status
        self.__model = model
        self.__make = make
        self.__manufacturing_year = manufacturing_year
        self.__mileage = mileage
        self.__log = []

    def reserve_vehicle(self):
        None

    def return_vehicle(self):
        None

class Car(Vehicle):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof, status, model, make, manufacturing_year,
                 mileage, type):
        super().__init__(license_num, stock_num, capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = type

class Van(Vehicle):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof, status, model, make, manufacturing_year,
                 mileage, type):
        super().__init__(license_num, stock_num, capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = type

class Truck(Vehicle):
    def __init__(self, license_num, stock_num, capacity, barcode, has_sunroof, status, model, make, manufacturing_year,
                 mileage, type):
        super().__init__(license_num, stock_num, capacity, barcode,
                         has_sunroof, status, model, make, manufacturing_year, mileage)
        self.__type = type


# We can have similar definition for other vehicle types

# ...
class VehicleLog:
    def __init__(self, id, type, description, creation_date):
        self.__id = id
        self.__type = type
        self.__description = description
        self.__creation_date = creation_date

    def update(self):
        None

    def search_by_log_type(self, type):
        None

class VehicleReservation:
    def __init__(self, reservation_number):
        self.__reservation_number = reservation_number
        self.__creation_date = datetime.date.today()
        self.__status = ReservationStatus.ACTIVE
        self.__due_date = datetime.date.today()
        self.__return_date = datetime.date.today()
        self.__pickup_location_name = ""
        self.__return_location_name = ""

        self.__customer_id = 0
        self.__vehicle = None
        self.__bill = None
        self.__additional_drivers = []
        self.__notifications = []
        self.__insurances = []
        self.__equipments = []
        self.__services = []

    def fetch_reservation_details(self, reservation_number):
        None

    def get_additional_drivers(self):
        return self.__additional_drivers

class Search(ABC):
    def search_by_type(self, type):
        None

    def search_by_model(self, model):
        None
    
class VehicleInventory(Search):
    def __init__(self):
        self.__vehicle_types = {}
        self.__vehicle_models = {}

    def search_by_type(self, query):
        # return all vehicles of the given type.
        return self.__vehicle_types.get(query)

    def search_by_model(self, query):
        # return all vehicles of the given model.
        return self.__vehicle_models.get(query)
    
from datetime import datetime

class Car:
    def __init__(self, car_id, model, year, price_per_hour, is_available=True):
        self.car_id = car_id
        self.model = model
        self.year = year
        self.price_per_hour = price_per_hour
        self.is_available = is_available

    def __str__(self):
        return f"Car ID: {self.car_id}\nModel: {self.model}\nYear: {self.year}\nPrice per hour: ${self.price_per_hour:.2f}\nAvailability: {'Available' if self.is_available else 'Not Available'}"


class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nAddress: {self.address}"


class Rental:
    def __init__(self, car, customer, start_time, duration_hours):
        self.car = car
        self.customer = customer
        self.start_time = start_time
        self.duration_hours = duration_hours

    def calculate_total_cost(self):
        return self.car.price_per_hour * self.duration_hours

    def __str__(self):
        return f"Rental Details:\n{self.customer}\n{self.car}\nStart Time: {self.start_time}\nDuration: {self.duration_hours} hours\nTotal Cost: ${self.calculate_total_cost():.2f}"


class Reservation:
    def __init__(self, car, customer, start_time, end_time):
        self.car = car
        self.customer = customer
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Reservation Details:\n{self.customer}\n{self.car}\nStart Time: {self.start_time}\nEnd Time: {self.end_time}"


# Usage example
car1 = Car("C001", "Honda Civic", 2022, 10.0)
car2 = Car("C002", "Toyota Corolla", 2021, 12.0)

customer1 = Customer("CUS001", "John Doe", "123 Main Street")
customer2 = Customer("CUS002", "Jane Smith", "456 Elm Street")

current_time = datetime.now()

rental1 = Rental(car1, customer1, current_time, 4)
rental2 = Rental(car2, customer2, current_time, 6)

reservation = Reservation(car1, customer2, current_time, current_time.replace(hour=current_time.hour + 2))

print(rental1)
print("\n")
print(rental2)
print("\n")
print(reservation)
