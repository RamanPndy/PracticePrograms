# Create coffee machine and refill ingredients
from systemdesign.cofee_machine.services import CoffeeMachine

coffee_machine = CoffeeMachine()
coffee_machine.refill_ingredient("Water", 500)
coffee_machine.refill_ingredient("Milk", 300)
coffee_machine.refill_ingredient("Coffee Beans", 200)
coffee_machine.refill_ingredient("Foam", 100)

# Select beverage and dispense
coffee_machine.select_beverage("Latte")
coffee_machine.dispense_beverage()
