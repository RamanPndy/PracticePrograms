from systemdesign.cofee_machine.interface import IBeverage
from systemdesign.cofee_machine.models import Cappuccino, Espresso, Latte

class BeverageFactory:
    @staticmethod
    def create_beverage(beverage_type: str) -> IBeverage:
        if beverage_type == "Espresso":
            return Espresso()
        elif beverage_type == "Latte":
            return Latte()
        elif beverage_type == "Cappuccino":
            return Cappuccino()
        else:
            raise ValueError(f"Beverage type '{beverage_type}' is not recognized.")
