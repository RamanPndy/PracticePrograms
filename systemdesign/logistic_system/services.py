from datetime import datetime
from typing import List
from systemdesign.log_tracking_system.interface import IObserver, ISubject
from systemdesign.logistic_system.interface import ITrackingService
from systemdesign.logistic_system.models import Container, Location, Order, Shipment, Stakeholder


class LogisticService(ISubject):
    def __init__(self):
        self.observers: List[IObserver] = []
        self.shipments: List[Shipment] = []
        self.orders: List[Order] = []

    def register_observer(self, observer: IObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: IObserver):
        self.observers.remove(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)

    def add_shipment(self, shipment: Shipment):
        self.shipments.append(shipment)
        self.notify_observers(f"New shipment added: {shipment.shipment_id}")

    def add_order(self, order: Order):
        self.orders.append(order)
        self.notify_observers(f"New order added: {order.order_id}")

class TrackingService(ITrackingService):
    def get_realtime_location(self, container: Container) -> Location:
        # Here, you'd integrate with an actual tracking system
        return container.current_location

class ETAService:
    def calculate_eta(self, shipment: Shipment) -> datetime:
        # Implement logic to calculate ETA based on distance, speed, etc.
        return datetime.now()

class NotificationService(IObserver):
    def __init__(self, stakeholder: Stakeholder):
        self.stakeholder = stakeholder

    def update(self, message: str):
        self.send_notification(message)

    def send_notification(self, message: str):
        print(f"Notification to {self.stakeholder.name}: {message}")
