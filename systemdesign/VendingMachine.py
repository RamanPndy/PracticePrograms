class Item:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

class VendingMachine:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, price, quantity):
        item = Item(item_id, name, price, quantity)
        self.items[item_id] = item

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]

    def purchase_item(self, item_id, amount):
        item = self.items.get(item_id)
        if not item:
            print("Item not found.")
            return None
        if item.quantity == 0:
            print("Item out of stock.")
            return None
        if amount < item.price:
            print("Insufficient amount.")
            return None
        item.quantity -= 1
        change = amount - item.price
        if change > 0:
            print(f"Dispensing item: {item.name}, change: {change}")
        else:
            print(f"Dispensing item: {item.name}")
        return item

# Example usage
if __name__ == "__main__":
    vending_machine = VendingMachine()

    # Add items
    vending_machine.add_item(1, "Soda", 1.50, 5)
    vending_machine.add_item(2, "Chips", 1.00, 3)
    vending_machine.add_item(3, "Candy", 0.75, 2)

    # Purchase items
    item1 = vending_machine.purchase_item(1, 2.00)
    item2 = vending_machine.purchase_item(2, 1.50)
    item3 = vending_machine.purchase_item(3, 1.00)

    # Remove an item
    vending_machine.remove_item(3)

    # Attempt to purchase a removed item
    item4 = vending_machine.purchase_item(3, 1.00)
