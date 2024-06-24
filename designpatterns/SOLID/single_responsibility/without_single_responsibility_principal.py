'''
In this example, the Invoice class has two responsibilities:
Calculating the total amount.
Printing the invoice details.
'''
class Invoice:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

    def print_invoice(self):
        total = self.calculate_total()
        print("Invoice Details")
        for item in self.items:
            print(f"{item['name']} - {item['quantity']} x ${item['price']}")
        print(f"Total: ${total}")

items = [
    {"name": "Widget", "price": 10, "quantity": 2},
    {"name": "Gadget", "price": 20, "quantity": 1}
]

invoice = Invoice(items)
invoice.print_invoice()