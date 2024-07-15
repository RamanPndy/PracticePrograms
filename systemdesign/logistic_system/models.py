from datetime import datetime
from typing import List, Optional

class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

class Stakeholder:
    def __init__(self, stakeholder_id: int, name: str, email: str):
        self.stakeholder_id = stakeholder_id
        self.name = name
        self.email = email

class Container:
    def __init__(self, container_id: int, capacity: int):
        self.container_id = container_id
        self.capacity = capacity
        self.current_location: Optional[Location] = None

class Shipment:
    def __init__(self, shipment_id: int, origin: Location, destination: Location, containers: List[Container]):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.containers = containers
        self.status: str = "Pending"
        self.eta: Optional[datetime] = None

class Order:
    def __init__(self, order_id: int, shipments: List[Shipment]):
        self.order_id = order_id
        self.shipments = shipments
