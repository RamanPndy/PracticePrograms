from systemdesign.cab_location.impl import ConcreteCab, ConcreteCabFinder, ConcreteDriver, ConcreteLocation, ConcreteTrip

'''
Design Patterns Used
Strategy Pattern: The CabFinder class can use different strategies to find nearby cabs (e.g., based on distance, 
traffic conditions, etc.). If different strategies are needed for calculating routes or managing trips.
Interface Segregation: Using interfaces to define the contract for location and cab operations.
Factory Pattern: (Optional) You can use the Factory pattern to create instances of drivers, trips, cabs and locations if there 
are multiple types of these entities.
State Pattern: To manage the state of the trip (e.g., started, in-progress, ended).
Observer Pattern: Can be used if you need to notify observers (e.g., a central tracking system) about location updates.
'''
if __name__ == "__main__":
    user_location = ConcreteLocation(12.9715987, 77.594566)
    cab1 = ConcreteCab(1, ConcreteLocation(12.9715987, 77.594566))
    cab2 = ConcreteCab(2, ConcreteLocation(12.9611159, 77.638322))
    cab3 = ConcreteCab(3, ConcreteLocation(12.959172, 77.697418))

    cabs = [cab1, cab2, cab3]
    cab_finder = ConcreteCabFinder(cabs)

    nearby_cabs = cab_finder.find_nearby_cabs(user_location, 5)  # 5 km radius

    for cab in nearby_cabs:
        print(f"Cab ID: {cab.get_id()} is within 5 km radius")

    driver = ConcreteDriver("D1")
    source = ConcreteLocation(12.9715987, 77.594566)
    destination = ConcreteLocation(13.0358, 77.5970)

    driver.update_location(source)

    trip = ConcreteTrip()
    trip.start_trip(driver, source, destination)

    # Update driver location during the trip
    intermediate_location = ConcreteLocation(12.9987, 77.6000)
    driver.update_location(intermediate_location)

    # End the trip
    trip.end_trip()

    # Get trip details
    trip_details = trip.get_trip_details()
    print(trip_details)
