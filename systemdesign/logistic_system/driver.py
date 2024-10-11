# Example usage
from systemdesign.logistic_system.models import Container, Location, Order, Shipment, Stakeholder
from systemdesign.logistic_system.services import ETAService, LogisticService, NotificationService, TrackingService

origin = Location(12.9716, 77.5946)
destination = Location(28.7041, 77.1025)
container = Container(1, 100)
shipment = Shipment(1, origin, destination, [container])
order = Order(1, [shipment])

stakeholder = Stakeholder(1, "Alice", "alice@example.com")
logistic_service = LogisticService()
notification_service = NotificationService(stakeholder)
logistic_service.register_observer(notification_service)

logistic_service.add_shipment(shipment)
logistic_service.add_order(order)

# Tracking
tracking_service = TrackingService()
container.current_location = Location(22.5726, 88.3639)
print(tracking_service.get_realtime_location(container))

# ETA Calculation
eta_service = ETAService()
shipment.eta = eta_service.calculate_eta(shipment)
print(f"ETA for shipment {shipment.shipment_id}: {shipment.eta}")
