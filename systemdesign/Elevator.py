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

    
class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.current_floor = 1
        self.is_moving = False
        self.destination_floors = []

    def add_destination_floor(self, floor):
        if floor not in self.destination_floors:
            self.destination_floors.append(floor)
            self.destination_floors.sort()

    def move(self):
        if not self.is_moving and self.destination_floors:
            self.is_moving = True
            while self.destination_floors:
                next_floor = self.destination_floors.pop(0)
                self.move_to_floor(next_floor)
            self.is_moving = False

    def move_to_floor(self, floor):
        if floor == self.current_floor:
            print(f"Elevator is already on floor {floor}.")
        elif floor < 1 or floor > self.num_floors:
            print(f"Invalid floor {floor}.")
        else:
            direction = "up" if floor > self.current_floor else "down"
            print(f"Elevator moving {direction} from floor {self.current_floor} to floor {floor}.")
            self.current_floor = floor
            print(f"Elevator arrived at floor {floor}.")

    def __str__(self):
        return f"Elevator is currently on floor {self.current_floor}."


class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.is_called = False

    def call_elevator(self, elevator):
        if not self.is_called:
            self.is_called = True
            elevator.add_destination_floor(self.floor_number)
            print(f"Elevator called to floor {self.floor_number}.")

    def __str__(self):
        return f"Floor {self.floor_number}."


class Passenger:
    def __init__(self, name, current_floor, destination_floor):
        self.name = name
        self.current_floor = current_floor
        self.destination_floor = destination_floor

    def request_elevator(self, elevator):
        if self.current_floor == elevator.current_floor:
            print(f"{self.name} is already on floor {self.current_floor}.")
        else:
            floor = Floor(self.current_floor)
            floor.call_elevator(elevator)
            print(f"{self.name} called the elevator from floor {self.current_floor}.")

    def enter_elevator(self, elevator):
        if self.current_floor == elevator.current_floor:
            print(f"{self.name} entered the elevator.")
            elevator.add_destination_floor(self.destination_floor)
        else:
            print(f"{self.name} is not on the current floor of the elevator.")

    def exit_elevator(self, elevator):
        if self.destination_floor == elevator.current_floor:
            print(f"{self.name} exited the elevator.")
        else:
            print(f"{self.name} cannot exit the elevator on the current floor.")


# Usage example
elevator = Elevator(num_floors=10)

# Create passengers
passenger1 = Passenger("Alice", 5, 2)
passenger2 = Passenger("Bob", 7, 10)
passenger3 = Passenger("Charlie", 3, 8)

# Passengers request the elevator
passenger1.request_elevator(elevator)
passenger2.request_elevator(elevator)
passenger3.request_elevator(elevator)

# Move the elevator
elevator.move()

# Passengers enter the elevator
passenger1.enter_elevator(elevator)
passenger2.enter_elevator(elevator)
passenger3.enter_elevator(elevator)

# Move the elevator
elevator.move()

# Passengers exit the elevator
passenger1.exit_elevator(elevator)
passenger2.exit_elevator(elevator)
passenger3.exit_elevator(elevator)
