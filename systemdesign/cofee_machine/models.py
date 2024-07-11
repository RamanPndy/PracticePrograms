from systemdesign.cofee_machine.interface import IBeverage, IInventory

class Espresso(IBeverage):
    def get_name(self) -> str:
        return "Espresso"

    def get_recipe(self) -> dict:
        return {"Water": 50, "Coffee Beans": 30}

class Latte(IBeverage):
    def get_name(self) -> str:
        return "Latte"

    def get_recipe(self) -> dict:
        return {"Water": 50, "Milk": 100, "Coffee Beans": 30}

class Cappuccino(IBeverage):
    def get_name(self) -> str:
        return "Cappuccino"

    def get_recipe(self) -> dict:
        return {"Water": 50, "Milk": 100, "Coffee Beans": 30, "Foam": 20}

class Inventory(IInventory):
    def __init__(self):
        self._ingredients = {}

    def add_ingredient(self, ingredient: str, quantity: int):
        if ingredient in self._ingredients:
            self._ingredients[ingredient] += quantity
        else:
            self._ingredients[ingredient] = quantity

    def use_ingredient(self, ingredient: str, quantity: int) -> bool:
        if ingredient in self._ingredients and self._ingredients[ingredient] >= quantity:
            self._ingredients[ingredient] -= quantity
            return True
        return False

    def get_quantity(self, ingredient: str) -> int:
        return self._ingredients.get(ingredient, 0)
