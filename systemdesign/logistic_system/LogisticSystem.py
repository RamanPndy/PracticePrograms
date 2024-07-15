class Warehouse:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = {}

    def add_product(self, product, quantity):
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity

    def remove_product(self, product, quantity):
        if product in self.inventory:
            if self.inventory[product] >= quantity:
                self.inventory[product] -= quantity
                return True
            else:
                print(f"Not enough {product} in {self.name}.")
        else:
            print(f"{product} not found in {self.name}.")
        return False

    def __str__(self):
        return f"Warehouse {self.name} located at {self.location}."


class Product:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"Product {self.name} (Weight: {self.weight} kg)."


class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products

    def calculate_total_weight(self):
        total_weight = 0
        for product, quantity in self.products.items():
            total_weight += product.weight * quantity
        return total_weight

    def __str__(self):
        return f"Order {self.order_id}."


class DeliveryRoute:
    def __init__(self, order, origin, destination):
        self.order = order
        self.origin = origin
        self.destination = destination

    def deliver_order(self):
        print(f"Delivering {self.order} from {self.origin} to {self.destination}.")
        total_weight = self.order.calculate_total_weight()
        print(f"Total weight: {total_weight} kg.")

        if self.origin.remove_product(self.order.products, 1):
            print(f"{self.order} delivered successfully.")
        else:
            print(f"Failed to deliver {self.order}. Not enough inventory in {self.origin}.")

    def __str__(self):
        return f"Delivery route for {self.order}."


# Usage example
warehouse_a = Warehouse("Warehouse A", "Location A")
warehouse_b = Warehouse("Warehouse B", "Location B")

product_a = Product("Product A", 2.5)
product_b = Product("Product B", 1.8)
product_c = Product("Product C", 3.2)

warehouse_a.add_product(product_a, 10)
warehouse_a.add_product(product_b, 5)
warehouse_b.add_product(product_c, 8)

order_1 = Order("Order 1", {product_a: 3, product_c: 2})
order_2 = Order("Order 2", {product_b: 4})

delivery_route_1 = DeliveryRoute(order_1, warehouse_a, warehouse_b)
delivery_route_2 = DeliveryRoute(order_2, warehouse_b, warehouse_a)

delivery_route_1.deliver_order()
delivery_route_2.deliver_order()
