from systemdesign.vending_machine.interface import IItem, IState
from systemdesign.vending_machine.models import Item, Payment
from systemdesign.vending_machine.services import VendingMachine

class IdleState(IState):
    def __init__(self, vending_machine: VendingMachine):
        self._vending_machine = vending_machine

    def handle(self):
        print("Vending Machine is in idle state.")
        # Transition to the SelectingState for item selection
        self._vending_machine.set_state(SelectingState(self._vending_machine))

class SelectingState(IState):
    def __init__(self, vending_machine: VendingMachine):
        self._vending_machine = vending_machine

    def handle(self):
        print("Vending Machine is in selecting state.")
        # Here would be the logic for selecting an item
        selected_item = Item("Soda", 1.25)  # For demonstration purposes
        if self._vending_machine.get_inventory().get_quantity(selected_item) > 0:
            self._vending_machine.set_state(PaymentState(self._vending_machine, selected_item))
        else:
            self._vending_machine.set_state(OutOfStockState(self._vending_machine))

class PaymentState(IState):
    def __init__(self, vending_machine: VendingMachine, item: IItem):
        self._vending_machine = vending_machine
        self._item = item

    def handle(self):
        print(f"Vending Machine is in payment state for item: {self._item.get_name()}")
        payment_processor = Payment()
        if payment_processor.process_payment(self._item.get_price()):
            self._vending_machine.get_inventory().remove_item(self._item, 1)
            self._vending_machine.set_state(DispensingState(self._vending_machine, self._item))
        else:
            print("Payment failed. Returning to idle state.")
            self._vending_machine.set_state(IdleState(self._vending_machine))

class DispensingState(IState):
    def __init__(self, vending_machine: VendingMachine, item: IItem):
        self._vending_machine = vending_machine
        self._item = item

    def handle(self):
        print(f"Dispensing item: {self._item.get_name()}")
        # Logic for dispensing the item
        self._vending_machine.set_state(IdleState(self._vending_machine))

class OutOfStockState(IState):
    def __init__(self, vending_machine: VendingMachine):
        self._vending_machine = vending_machine

    def handle(self):
        print("Selected item is out of stock.")
        self._vending_machine.set_state(IdleState(self._vending_machine))

