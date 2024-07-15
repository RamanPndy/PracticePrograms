from systemdesign.pizza_delivery_system.interface import DeliveryService, OrderService, PizzaService, UserService
from systemdesign.pizza_delivery_system.models import Delivery, Order, Pizza, User


class UserServiceImpl(UserService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserServiceImpl, cls).__new__(cls)
            cls._instance.users = {}
        return cls._instance

    def register_user(self, name, address, email):
        user_id = len(self.users) + 1
        user = User(user_id, name, address, email)
        self.users[user_id] = user
        return user

    def get_user(self, user_id):
        return self.users.get(user_id)

class PizzaServiceImpl(PizzaService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PizzaServiceImpl, cls).__new__(cls)
            cls._instance.pizzas = {}
        return cls._instance

    def add_pizza(self, name, ingredients, price):
        pizza_id = len(self.pizzas) + 1
        pizza = Pizza(pizza_id, name, ingredients, price)
        self.pizzas[pizza_id] = pizza
        return pizza

    def get_pizza(self, pizza_id):
        return self.pizzas.get(pizza_id)

class OrderServiceImpl(OrderService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderServiceImpl, cls).__new__(cls)
            cls._instance.orders = {}
        return cls._instance

    def create_order(self, user, pizzas):
        order_id = len(self.orders) + 1
        total_price = sum(pizza.price for pizza in pizzas)
        order = Order(order_id, user, pizzas, total_price, "Pending")
        self.orders[order_id] = order
        return order

    def get_order(self, order_id):
        return self.orders.get(order_id)

class DeliveryServiceImpl(DeliveryService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DeliveryServiceImpl, cls).__new__(cls)
            cls._instance.deliveries = {}
        return cls._instance

    def assign_delivery(self, order, delivery_person):
        delivery_id = len(self.deliveries) + 1
        delivery = Delivery(delivery_id, order, delivery_person, "Assigned")
        self.deliveries[delivery_id] = delivery
        return delivery

    def update_delivery_status(self, delivery_id, status):
        delivery = self.deliveries.get(delivery_id)
        if delivery:
            delivery.status = status
        return delivery
