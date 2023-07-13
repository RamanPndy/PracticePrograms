'''
the cart management service consists of the User, Product, Cart, and CartManagementService classes. 
The User class represents users with unique IDs and names. The Product class represents products with 
unique IDs, names, and prices. The Cart class represents individual user carts with items and 
quantities. The CartManagementService class manages users and their carts, providing methods to add 
users, add products to carts, remove products from carts, and retrieve cart details.
'''
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.cart = Cart()

    def __str__(self):
        return f"User ID: {self.user_id}\nName: {self.name}"


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nPrice: {self.price}"


class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product, quantity):
        if product in self.items:
            if self.items[product] >= quantity:
                self.items[product] -= quantity
                if self.items[product] == 0:
                    del self.items[product]
            else:
                print(f"Not enough {product.name} in the cart.")
        else:
            print(f"{product.name} is not present in the cart.")

    def get_total_cost(self):
        total_cost = 0
        for product, quantity in self.items.items():
            total_cost += product.price * quantity
        return total_cost

    def __str__(self):
        return f"Cart:\nItems: {', '.join([f'{product.name} x {quantity}' for product, quantity in self.items.items()])}\nTotal Cost: {self.get_total_cost()}"


class CartManagementService:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def add_product_to_cart(self, user_id, product, quantity):
        if user_id in self.users:
            user = self.users[user_id]
            user.cart.add_item(product, quantity)
            print(f"Product added to the cart successfully.")
        else:
            print(f"User with ID {user_id} not found.")

    def remove_product_from_cart(self, user_id, product, quantity):
        if user_id in self.users:
            user = self.users[user_id]
            user.cart.remove_item(product, quantity)
            print(f"Product removed from the cart successfully.")
        else:
            print(f"User with ID {user_id} not found.")

    def get_cart_details(self, user_id):
        if user_id in self.users:
            user = self.users[user_id]
            return user.cart
        else:
            return None

    def __str__(self):
        return f"Cart Management Service\nTotal Users: {len(self.users)}"


# Usage example
user1 = User("U001", "John Doe")
user2 = User("U002", "Jane Smith")

product1 = Product("P001", "Product A", 10.0)
product2 = Product("P002", "Product B", 15.0)
product3 = Product("P003", "Product C", 8.0)

cart_management_service = CartManagementService()
cart_management_service.add_user(user1)
cart_management_service.add_user(user2)

cart_management_service.add_product_to_cart("U001", product1, 2)
cart_management_service.add_product_to_cart("U001", product2, 1)
cart_management_service.add_product_to_cart("U002", product3, 3)

cart_management_service.remove_product_from_cart("U001", product1, 1)
cart_management_service.remove_product_from_cart("U002", product2, 2)

print(cart_management_service)
print("\n")
print(user1.cart)
print("\n")
print(user2.cart)
