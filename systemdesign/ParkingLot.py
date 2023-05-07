class Address:
    def __init__(self, street, block, city, state, country) -> None:
        self.street = street
        self.block = block
        self.city = city
        self.state = state
        self.country = country

class ParkingFloor:
    def __init__(self, name) -> None:
        self.name = name
        self.parkingSlots = dict()