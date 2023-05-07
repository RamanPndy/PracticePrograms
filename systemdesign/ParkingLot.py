import time

class Address:
    def __init__(self, street, block, city, state, country) -> None:
        self.street = street
        self.block = block
        self.city = city
        self.state = state
        self.country = country

class ParkingSlotType:
    TWOWHEELER = 0.05
    COMPACT = 0.075
    MEDIUM = 0.09
    LARGE = 0.10
        
    def getPriceForParking(self, parkingType, duration):
        return parkingType * duration

class ParkingSlot:
    def __init__(self, name, parkingSlotType) -> None:
        self.name = name
        self.parkingSlotType = parkingSlotType
        self.vehicle = None
        self.isAvailable = True

    def addVehicle(self, vehicle):
        self.vehicle = vehicle
        self.isAvailable = False

    def removeVehicle(self, vehicle):
        self.vehicle = vehicle
        self.isAvailable = False

class VehicleCategory:
    TWOWHEELER = 1
    SEDAN = 2
    HATCHBACK = 3
    SUV = 4
    BUS = 5

class Vehicle:
    def __init__(self, vehicleNumber, category) -> None:
        self.vehicleNumber = vehicleNumber
        self.vehicleCategory = category
        
class ParkingFloor:
    def __init__(self, name) -> None:
        self.name = name
        self.parkingSlots = dict() # Map of Map Map{ParkingSlotType : Map{String, ParkingSlot}}

    def getRelevantSlotForVehicleAndPark(self, vehicle):
        parkingSlotType = self.pickCorrectSlot(vehicle.vehicleCategory)
        relevantParkingSlot = self.parkingSlots.get(parkingSlotType)
        for floor, parkingSlot in relevantParkingSlot:
            if parkingSlot.isAvailable():
                parkingSlot.addVehicle(vehicle)
                return parkingSlot
    
    def pickCorrectSlot(self, vehicleCategory):
        if vehicleCategory == VehicleCategory.TWOWHEELER:
            return ParkingSlotType.TWOWHEELER
        elif vehicleCategory == VehicleCategory.SUV:
            return ParkingSlotType.MEDIUM
        elif vehicleCategory == VehicleCategory.BUS:
            return ParkingSlotType.LARGE
        elif vehicleCategory == VehicleCategory.HATCHBACK or vehicleCategory == VehicleCategory.SEDAN:
            return ParkingSlotType.COMPACT

class Ticket:
    def __init__(self, parkingSlot, vehicle) -> None:
        self.ticketNumber = vehicle.vehicleNumber + time.now()
        self.parkingSlot = parkingSlot
        self.vehicle = vehicle
        self.startTime = time.now()

class ParkingLot:
    #it would be Singleton class
    def __init__(self, nameOfParkingLot) -> None:
        self.parkingFloors = list()
        self.nameOfParkingLot = nameOfParkingLot
        
    def getParkingSlotForVehicleAndPark(self, vehicle):
        for floor in self.parkingFloors:
            slot = floor.getRelevantSlotForVehicleAndPark(vehicle)
            if slot is not None:
                return slot
    
    def assignTicket(self, vehicle):
        parkingSlot = self.getParkingSlotForVehicleAndPark(vehicle)
        if parkingSlot is not None:
            parkingTicket = self.createTicketForSlot(parkingSlot, vehicle)
            return parkingTicket
    
    def scanAndPay(self, ticket):
        endTime = time.now()
        ticket.parkingSlot.removeVehicle(ticket.vehicle)
        duration = (endTime - ticket.startTime) / 1000
        price = ticket.parkingSlot.parkingSlotType.getPriceForParking(ticket.parkingSlot.parkingSlotType, duration)
        return price

    def createTicketForSlot(self, parkingSlot, vehicle):
        return Ticket(parkingSlot, vehicle)