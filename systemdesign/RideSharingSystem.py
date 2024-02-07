import uuid
from datetime import datetime

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Driver:
    def __init__(self, driver_id, name, vehicle):
        self.driver_id = driver_id
        self.name = name
        self.vehicle = vehicle

class Ride:
    def __init__(self, ride_id, user, pickup_location, dropoff_location):
        self.ride_id = ride_id
        self.user = user
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.driver = None
        self.status = "Requested"
        self.fare = None
        self.timestamp = datetime.now()

class RideSharingSystem:
    def __init__(self):
        self.users = {}
        self.drivers = {}
        self.rides = []

    def add_user(self, name):
        user_id = str(uuid.uuid4())
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def add_driver(self, name, vehicle):
        driver_id = str(uuid.uuid4())
        driver = Driver(driver_id, name, vehicle)
        self.drivers[driver_id] = driver
        return driver

    def request_ride(self, user_id, pickup_location, dropoff_location):
        user = self.users.get(user_id)
        if user:
            ride_id = str(uuid.uuid4())
            ride = Ride(ride_id, user, pickup_location, dropoff_location)
            self.rides.append(ride)
            return ride
        else:
            print("User not found.")

    def assign_driver(self, ride_id, driver_id):
        ride = next((r for r in self.rides if r.ride_id == ride_id), None)
        driver = self.drivers.get(driver_id)
        if ride and driver:
            ride.driver = driver
            ride.status = "Assigned"
        else:
            print("Ride or driver not found.")

    def start_ride(self, ride_id):
        ride = next((r for r in self.rides if r.ride_id == ride_id), None)
        if ride and ride.status == "Assigned":
            ride.status = "In Progress"
            ride.timestamp = datetime.now()
        else:
            print("Ride not found or not in assigned status.")

    def end_ride(self, ride_id, fare):
        ride = next((r for r in self.rides if r.ride_id == ride_id), None)
        if ride and ride.status == "In Progress":
            ride.status = "Completed"
            ride.fare = fare
        else:
            print("Ride not found or not in progress status.")

# Example usage
if __name__ == "__main__":
    ride_sharing_system = RideSharingSystem()

    # Add users
    user1 = ride_sharing_system.add_user("Alice")
    user2 = ride_sharing_system.add_user("Bob")

    # Add drivers
    driver1 = ride_sharing_system.add_driver("John", "Car")
    driver2 = ride_sharing_system.add_driver("Mary", "Bike")

    # Request ride
    ride1 = ride_sharing_system.request_ride(user1.user_id, "Home", "Work")

    # Assign driver
    ride_sharing_system.assign_driver(ride1.ride_id, driver1.driver_id)

    # Start ride
    ride_sharing_system.start_ride(ride1.ride_id)

    # End ride
    ride_sharing_system.end_ride(ride1.ride_id, 20)

    # Display ride details
    print(f"Ride ID: {ride1.ride_id}")
    print(f"User: {ride1.user.name}")
    print(f"Driver: {ride1.driver.name}")
    print(f"Pickup Location: {ride1.pickup_location}")
    print(f"Dropoff Location: {ride1.dropoff_location}")
    print(f"Status: {ride1.status}")
    print(f"Fare: {ride1.fare}")
    print(f"Timestamp: {ride1.timestamp}")
