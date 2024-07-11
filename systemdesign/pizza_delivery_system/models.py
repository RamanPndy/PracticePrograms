class User:
    def __init__(self, user_id, name, address, email):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.email = email

class Pizza:
    def __init__(self, pizza_id, name, ingredients, price):
        self.pizza_id = pizza_id
        self.name = name
        self.ingredients = ingredients
        self.price = price

class Order:
    def __init__(self, order_id, user, pizzas, total_price, status):
        self.order_id = order_id
        self.user = user
        self.pizzas = pizzas
        self.total_price = total_price
        self.status = status

class Delivery:
    def __init__(self, delivery_id, order, delivery_person, status):
        self.delivery_id = delivery_id
        self.order = order
        self.delivery_person = delivery_person
        self.status = status
