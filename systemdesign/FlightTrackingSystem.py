'''
the flight tracking system consists of Flight, Airport, and FlightTracker classes. 
The Flight class represents individual flights with flight numbers, departure and arrival airports, and departure and 
arrival times. 
The Airport class represents airports with airport codes and locations. 
The FlightTracker class maintains a list of flights and provides methods to add flights and track a 
specific flight by its flight number.
'''
class Flight:
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time):
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __str__(self):
        return f"Flight Number: {self.flight_number}\nDeparture: {self.departure_airport}\nArrival: {self.arrival_airport}\nDeparture Time: {self.departure_time}\nArrival Time: {self.arrival_time}"


class Airport:
    def __init__(self, airport_code, location):
        self.airport_code = airport_code
        self.location = location

    def __str__(self):
        return f"Airport: {self.airport_code}\nLocation: {self.location}"


class FlightTracker:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def track_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                print(f"Tracking Flight {flight_number}...")
                print(f"{flight}\n")
                return
        print(f"Flight {flight_number} not found.")

    def __str__(self):
        return f"Flight Tracker\nTotal Flights: {len(self.flights)}"


# Usage example
airport1 = Airport("ABC", "Location A")
airport2 = Airport("XYZ", "Location X")

flight1 = Flight("F001", airport1, airport2, "12:00 PM", "2:00 PM")
flight2 = Flight("F002", airport2, airport1, "3:00 PM", "5:00 PM")

tracker = FlightTracker()
tracker.add_flight(flight1)
tracker.add_flight(flight2)

print(tracker)
tracker.track_flight("F001")
tracker.track_flight("F003")
