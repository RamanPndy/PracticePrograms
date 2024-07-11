from abc import ABC, abstractmethod

class UserService(ABC):
    @abstractmethod
    def register_user(self, name, address, email):
        pass

    @abstractmethod
    def get_user(self, user_id):
        pass

class PizzaService(ABC):
    @abstractmethod
    def add_pizza(self, name, ingredients, price):
        pass

    @abstractmethod
    def get_pizza(self, pizza_id):
        pass

class OrderService(ABC):
    @abstractmethod
    def create_order(self, user, pizzas):
        pass

    @abstractmethod
    def get_order(self, order_id):
        pass

class DeliveryService(ABC):
    @abstractmethod
    def assign_delivery(self, order, delivery_person):
        pass

    @abstractmethod
    def update_delivery_status(self, delivery_id, status):
        pass
