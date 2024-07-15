from systemdesign.vending_machine.interface import IInventory, IItem, IPayment

class Item(IItem):
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def __repr__(self):
        return f"Item(name='{self._name}', price={self._price})"

class Inventory(IInventory):
    def __init__(self):
        self._inventory = {}

    def add_item(self, item: IItem, quantity: int):
        if item in self._inventory:
            self._inventory[item] += quantity
        else:
            self._inventory[item] = quantity

    def remove_item(self, item: IItem, quantity: int) -> bool:
        if item in self._inventory and self._inventory[item] >= quantity:
            self._inventory[item] -= quantity
            return True
        return False

    def get_quantity(self, item: IItem) -> int:
        return self._inventory.get(item, 0)

class Payment(IPayment):
    def process_payment(self, amount: float) -> bool:
        # Here we would have actual payment processing logic.
        # For simplicity, let's assume the payment always succeeds.
        return True
