from abc import ABC, abstractmethod

class Location(ABC):
    @abstractmethod
    def get_coordinates(self):
        pass

class Cab(ABC):
    @abstractmethod
    def get_location(self):
        pass

    @abstractmethod
    def get_id(self):
        pass

class CabFinder(ABC):
    @abstractmethod
    def find_nearby_cabs(self, user_location, radius):
        pass

class Trip(ABC):
    @abstractmethod
    def start_trip(self, driver, source, destination):
        pass

    @abstractmethod
    def end_trip(self):
        pass

    @abstractmethod
    def get_trip_details(self):
        pass

class Driver(ABC):
    @abstractmethod
    def get_current_location(self):
        pass

    @abstractmethod
    def start_trip(self, trip):
        pass

    @abstractmethod
    def end_trip(self):
        pass

    @abstractmethod
    def update_location(self, location):
        pass
