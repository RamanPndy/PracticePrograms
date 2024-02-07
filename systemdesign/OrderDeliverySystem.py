from enum import Enum
from abc import ABC, abstractmethod
import uuid
from datetime import datetime, timedelta

# Enum for Order Status
class OrderStatus(Enum):
    PLACED = "Placed"
    CONFIRMED = "Confirmed"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

# Enum for Delivery Personnel Status
class DeliveryPersonnelStatus(Enum):
    AVAILABLE = "Available"
    BUSY = "Busy"

# Abstract class for Delivery Personnel
class DeliveryPersonnel(ABC):
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.status = DeliveryPersonnelStatus.AVAILABLE

    @abstractmethod
    def deliver_order(self, order):
        pass

# Class for Bike Delivery Personnel
class BikeDeliveryPersonnel(DeliveryPersonnel):
    def __init__(self, name):
        super().__init__(name)
        self.vehicle = "Bike"

    def deliver_order(self, order):
        self.status = DeliveryPersonnelStatus.BUSY
        delivery_time = datetime.now() + timedelta(minutes=30)  # Assuming 30 minutes delivery time
        order.delivery_time = delivery_time
        order.status = OrderStatus.IN_TRANSIT
        print(f"{self.name} on {self.vehicle} is delivering Order ID: {order.id}")
        print(f"Estimated Delivery Time: {delivery_time}")
        self.status = DeliveryPersonnelStatus.AVAILABLE

# Class for Order
class Order:
    def __init__(self, customer_name, items):
        self.id = str(uuid.uuid4())
        self.customer_name = customer_name
        self.items = items
        self.status = OrderStatus.PLACED
        self.delivery_time = None

    def confirm_order(self):
        self.status = OrderStatus.CONFIRMED

# Class for Order Delivery System
class OrderDeliverySystem:
    def __init__(self):
        self.orders = []
        self.delivery_personnel = []

    def place_order(self, customer_name, items):
        order = Order(customer_name, items)
        self.orders.append(order)
        print(f"Order ID: {order.id} placed successfully.")
        return order

    def confirm_order(self, order_id):
        order = next((order for order in self.orders if order.id == order_id), None)
        if order:
            order.confirm_order()
            print(f"Order ID: {order_id} confirmed successfully.")
        else:
            print(f"Order ID: {order_id} not found.")

    def assign_delivery_personnel(self, delivery_personnel):
        self.delivery_personnel.append(delivery_personnel)
        print(f"Delivery personnel {delivery_personnel.name} added successfully.")

    def assign_delivery(self, order_id):
        order = next((order for order in self.orders if order.id == order_id), None)
        if order:
            available_personnel = [personnel for personnel in self.delivery_personnel if personnel.status == DeliveryPersonnelStatus.AVAILABLE]
            if available_personnel:
                delivery_personnel = available_personnel[0]
                delivery_personnel.deliver_order(order)
            else:
                print("No available delivery personnel.")
        else:
            print(f"Order ID: {order_id} not found.")

# Example Usage
if __name__ == "__main__":
    delivery_system = OrderDeliverySystem()

    # Add delivery personnel
    bike_delivery_person_1 = BikeDeliveryPersonnel("John")
    delivery_system.assign_delivery_personnel(bike_delivery_person_1)

    # Place an order
    order = delivery_system.place_order("Alice", ["Pizza", "Burger", "Coke"])

    # Confirm the order
    delivery_system.confirm_order(order.id)

    # Assign delivery
    delivery_system.assign_delivery(order.id)
