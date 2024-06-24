import math
from systemdesign.cab_location.interface import Cab, CabFinder, Driver, Location, Trip

class ConcreteLocation(Location):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinates(self):
        return (self.latitude, self.longitude)

class ConcreteCab(Cab):
    def __init__(self, cab_id, location):
        self.cab_id = cab_id
        self.location = location

    def get_location(self):
        return self.location

    def get_id(self):
        return self.cab_id

class ConcreteCabFinder(CabFinder):
    def __init__(self, cabs):
        self.cabs = cabs

    def haversine_distance(self, loc1, loc2):
        # Calculate the great circle distance between two points on the earth (specified in decimal degrees)
        lat1, lon1 = loc1.get_coordinates()
        lat2, lon2 = loc2.get_coordinates()
        
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        
        # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
        km = 6371 * c
        return km

    def find_nearby_cabs(self, user_location, radius):
        nearby_cabs = []
        for cab in self.cabs:
            cab_location = cab.get_location()
            distance = self.haversine_distance(user_location, cab_location)
            if distance <= radius:
                nearby_cabs.append(cab)
        return nearby_cabs

class ConcreteTrip(Trip):
    def __init__(self):
        self.driver = None
        self.source = None
        self.destination = None
        self.is_active = False

    def start_trip(self, driver, source, destination):
        self.driver = driver
        self.source = source
        self.destination = destination
        self.is_active = True
        driver.start_trip(self)
        print(f"Trip started from {source.get_coordinates()} to {destination.get_coordinates()}")

    def end_trip(self):
        self.is_active = False
        self.driver.end_trip()
        print(f"Trip ended at {self.destination.get_coordinates()}")

    def get_trip_details(self):
        return {
            "driver": self.driver,
            "source": self.source.get_coordinates(),
            "destination": self.destination.get_coordinates(),
            "is_active": self.is_active
        }

class ConcreteDriver(Driver):
    def __init__(self, driver_id):
        self.driver_id = driver_id
        self.current_location = None
        self.current_trip = None

    def get_current_location(self):
        return self.current_location

    def start_trip(self, trip):
        self.current_trip = trip

    def end_trip(self):
        self.current_trip = None

    def update_location(self, location):
        self.current_location = location
        print(f"Driver {self.driver_id} location updated to {location.get_coordinates()}")
