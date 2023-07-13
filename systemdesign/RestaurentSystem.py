class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.menu = {}

    def add_item_to_menu(self, item, price):
        self.menu[item] = price

    def remove_item_from_menu(self, item):
        if item in self.menu:
            del self.menu[item]
        else:
            print(f"{item} is not available in the menu.")

    def __str__(self):
        return f"Restaurant: {self.name}\nLocation: {self.location}\nMenu: {', '.join(self.menu.keys())}"


class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"User: {self.name}\nAddress: {self.address}"


class Order:
    def __init__(self, user):
        self.user = user
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.items:
            if self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
            else:
                print(f"Not enough {item} in the order.")
        else:
            print(f"{item} is not present in the order.")

    def calculate_total_cost(self, restaurant):
        total_cost = 0
        for item, quantity in self.items.items():
            if item in restaurant.menu:
                price = restaurant.menu[item]
                total_cost += price * quantity
        return total_cost

    def __str__(self):
        return f"Order details:\n{self.user}\nItems: {', '.join(self.items.keys())}"


class Delivery:
    def __init__(self, order, restaurant):
        self.order = order
        self.restaurant = restaurant

    def deliver(self):
        print(f"Delivering order to {self.order.user.name} at {self.order.user.address}.")
        total_cost = self.order.calculate_total_cost(self.restaurant)
        print(f"Total cost: ${total_cost:.2f}")

    def __str__(self):
        return f"Delivery for {self.order.user.name}"


# Usage example
restaurant = Restaurant("Restaurant A", "Location A")
restaurant.add_item_to_menu("Item 1", 10)
restaurant.add_item_to_menu("Item 2", 15)
restaurant.add_item_to_menu("Item 3", 8)

user = User("User A", "Address A")

order = Order(user)
order.add_item("Item 1", 2)
order.add_item("Item 3", 4)

delivery = Delivery(order, restaurant)
delivery.deliver()

print(restaurant)
print(order)
