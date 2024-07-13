from abc import ABC, abstractmethod

class IBeverage(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_recipe(self) -> dict:
        pass

class IInventory(ABC):
    @abstractmethod
    def add_ingredient(self, ingredient: str, quantity: int):
        pass

    @abstractmethod
    def use_ingredient(self, ingredient: str, quantity: int) -> bool:
        pass

    @abstractmethod
    def get_quantity(self, ingredient: str) -> int:
        pass

class ICoffeeMachine(ABC):
    @abstractmethod
    def select_beverage(self, beverage: str):
        pass

    @abstractmethod
    def dispense_beverage(self):
        pass

    @abstractmethod
    def refill_ingredient(self, ingredient: str, quantity: int):
        pass

