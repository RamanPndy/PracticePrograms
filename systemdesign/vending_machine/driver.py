# Create items
from systemdesign.vending_machine.models import Item
from systemdesign.vending_machine.services import VendingMachine

soda = Item("Soda", 1.25)
chips = Item("Chips", 1.50)

# Create vending machine and add items to inventory
vending_machine = VendingMachine()
vending_machine.get_inventory().add_item(soda, 10)
vending_machine.get_inventory().add_item(chips, 5)

# Handle state transitions
vending_machine.handle()  # IdleState -> SelectingState
vending_machine.handle()  # SelectingState -> PaymentState or OutOfStockState
vending_machine.handle()  # PaymentState -> DispensingState or back to IdleState on payment failure
vending_machine.handle()  # DispensingState -> IdleState
