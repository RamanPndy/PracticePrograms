from systemdesign.cofee_machine.factory import BeverageFactory
from systemdesign.cofee_machine.interface import ICoffeeMachine
from systemdesign.cofee_machine.models import Inventory

class CoffeeMachine(ICoffeeMachine):
    def __init__(self):
        self._inventory = Inventory()
        self._selected_beverage = None

    def select_beverage(self, beverage: str):
        self._selected_beverage = BeverageFactory.create_beverage(beverage)

    def dispense_beverage(self):
        if self._selected_beverage:
            recipe = self._selected_beverage.get_recipe()
            for ingredient, quantity in recipe.items():
                if not self._inventory.use_ingredient(ingredient, quantity):
                    print(f"Insufficient {ingredient}")
                    return
            print(f"Dispensing {self._selected_beverage.get_name()}")
        else:
            print("No beverage selected")

    def refill_ingredient(self, ingredient: str, quantity: int):
        self._inventory.add_ingredient(ingredient, quantity)
