'''
the generic order management system consists of the Customer, Product, Order, and OrderManagementSystem
classes. The Customer class represents customers with unique IDs, names, and addresses. The Product 
class represents products with unique IDs, names, and prices. The Order class represents individual 
orders with order IDs, customer details, product details, and quantities. The OrderManagementSystem 
class manages customers, products, and orders, providing methods to add customers, add products, 
place orders, cancel orders, and maintain the order ID counter.
'''
class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nAddress: {self.address}"


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nPrice: {self.price}"


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.products = {}

    def add_product(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product, quantity):
        if product in self.products:
            if self.products[product] >= quantity:
                self.products[product] -= quantity
                if self.products[product] == 0:
                    del self.products[product]
            else:
                print(f"Not enough {product.name} in the order.")
        else:
            print(f"{product.name} is not present in the order.")

    def calculate_total_cost(self):
        total_cost = 0
        for product, quantity in self.products.items():
            total_cost += product.price * quantity
        return total_cost

    def __str__(self):
        return f"Order ID: {self.order_id}\n{self.customer}\nProducts: {', '.join([f'{product.name} x {quantity}' for product, quantity in self.products.items()])}\nTotal Cost: {self.calculate_total_cost()}"


class OrderManagementSystem:
    def __init__(self):
        self.customers = {}
        self.products = {}
        self.orders = {}
        self.order_id_counter = 1

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def add_product(self, product):
        self.products[product.product_id] = product

    def place_order(self, customer_id, product_id, quantity):
        if customer_id in self.customers and product_id in self.products:
            customer = self.customers[customer_id]
            product = self.products[product_id]
            order = self.orders.get(self.order_id_counter, Order(self.order_id_counter, customer))
            order.add_product(product, quantity)
            self.orders[self.order_id_counter] = order
            self.order_id_counter += 1
            print(f"Order placed successfully.")
            return order
        else:
            print("Invalid customer ID or product ID.")
            return None

    def cancel_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            print(f"Order {order_id} cancelled successfully.")
        else:
            print(f"Order {order_id} not found.")

    def __str__(self):
        return f"Order Management System\nTotal Customers: {len(self.customers)}\nTotal Products: {len(self.products)}\nTotal Orders: {len(self.orders)}"


# Usage example
customer1 = Customer("C001", "John Doe", "123 Main Street")
customer2 = Customer("C002", "Jane Smith", "456 Elm Street")

product1 = Product("P001", "Product A", 10.0)
product2 = Product("P002", "Product B", 15.0)
product3 = Product("P003", "Product C", 8.0)

order_management_system = OrderManagementSystem()
order_management_system.add_customer(customer1)
order_management_system.add_customer(customer2)
order_management_system.add_product(product1)
order_management_system.add_product(product2)

order1 = order_management_system.place_order("C001", "P001", 2)
order2 = order_management_system.place_order("C002", "P002", 3)

order_management_system.cancel_order(1)
order_management_system.cancel_order(3)

print(order1)
print("\n")
print(order2)
print("\n")
print(order_management_system)
