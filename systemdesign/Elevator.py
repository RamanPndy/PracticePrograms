class Direction:
    UP = 1
    DOWN = 2

class State:
    IDLE = 1
    MOVING = 2
    STOPPED = 3
    OUTOFORDER = 4

class Elevator:
    def __init__(self, id) -> None:
        self.id = id
        self.currentFloor = 0
        self.direction = Direction.UP
        self.currentState = State.IDLE

class Display:
    def __init__(self) -> None:
        self.currentFloor = 0
        self.direction = Direction.UP

class Floor:
    def __init__(self, id) -> None:
        self.id = id
        self.door = list()

class InternalRequest:
    def __init__(self, destinationFloor) -> None:
        self.destinationFloor = destinationFloor

class ExternalRequest:
    def __init__(self, direction, sourceFloor) -> None:
        self.directionToGo = direction
        self.sourceFloor = sourceFloor

class Request:
    def __init__(self, internalReq, externalReq) -> None:
        self.internalReq = internalReq
        self.externalReq = externalReq

    def request(self, floor, direction):
        pass

class Building:
    def __init__(self) -> None:
        self.floors = list()
        self.elevators = list()

class Schedular:
    def __init__(self) -> None:
        self.requests = list()
    
    def dispatch(self, elevatorId, floor):
        pass

    