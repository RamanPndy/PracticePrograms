'''
Swiggy-like delivery system consists of Restaurant, Customer, Order, DeliveryExecutive, and 
DeliverySystem classes. 
The Restaurant class represents restaurants with names and locations. 
The Customer class represents customers with names and addresses. 
The Order class represents individual orders with order IDs, restaurant details, customer details, items, order time, and 
assigned delivery executive. 
The DeliveryExecutive class represents delivery executives with names and vehicles. 
The DeliverySystem class manages the orders and delivery executives, providing methods to 
place orders, assign delivery executives, and add delivery executives to the system.
'''
from datetime import datetime

class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"Restaurant: {self.name}\nLocation: {self.location}"


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Customer: {self.name}\nAddress: {self.address}"


class Order:
    def __init__(self, order_id, restaurant, customer, items):
        self.order_id = order_id
        self.restaurant = restaurant
        self.customer = customer
        self.items = items
        self.order_time = datetime.now()
        self.delivery_executive = None

    def assign_delivery_executive(self, delivery_executive):
        self.delivery_executive = delivery_executive

    def __str__(self):
        return f"Order ID: {self.order_id}\nRestaurant: {self.restaurant}\nCustomer: {self.customer}\nItems: {self.items}\nOrder Time: {self.order_time}\nDelivery Executive: {self.delivery_executive}"


class DeliveryExecutive:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    def __str__(self):
        return f"Delivery Executive: {self.name}\nVehicle: {self.vehicle}"


class DeliverySystem:
    def __init__(self):
        self.orders = []
        self.delivery_executives = []

    def place_order(self, order):
        self.orders.append(order)
        print(f"Order {order.order_id} placed successfully.")

    def assign_delivery_executive(self, order, delivery_executive):
        order.assign_delivery_executive(delivery_executive)
        print(f"Delivery executive {delivery_executive.name} assigned to order {order.order_id}.")

    def add_delivery_executive(self, delivery_executive):
        self.delivery_executives.append(delivery_executive)
        print(f"Delivery executive {delivery_executive.name} added to the system.")

    def __str__(self):
        return f"Delivery System\nTotal Orders: {len(self.orders)}\nTotal Delivery Executives: {len(self.delivery_executives)}"


# Usage example
restaurant = Restaurant("Restaurant A", "Location A")
customer = Customer("Customer A", "Address A")
order = Order("Order 1", restaurant, customer, ["Item 1", "Item 2"])

delivery_executive = DeliveryExecutive("John Doe", "Car")

system = DeliverySystem()
system.add_delivery_executive(delivery_executive)
system.place_order(order)
system.assign_delivery_executive(order, delivery_executive)

print(system)
print(order)
