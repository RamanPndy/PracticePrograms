'''
Explanation
Single Responsibility: The User class is now responsible only for managing user data. The UserRepository class is responsible 
for saving user data to the database.
Separation of Concerns: Changes in the user data structure will affect only the User class, while changes in the database 
logic will affect only the UserRepository class.
'''
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserRepository:
    def save_to_db(self, user):
        # Logic to save the user to a database
        print(f"Saving {user.username} to the database.")

user = User("john_doe", "john@example.com")
user_repo = UserRepository()
user_repo.save_to_db(user)

class Invoice:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

class InvoicePrinter:
    def print_invoice(self, invoice):
        total = invoice.calculate_total()
        print("Invoice Details")
        for item in invoice.items:
            print(f"{item['name']} - {item['quantity']} x ${item['price']}")
        print(f"Total: ${total}")

items = [
    {"name": "Widget", "price": 10, "quantity": 2},
    {"name": "Gadget", "price": 20, "quantity": 1}
]

invoice = Invoice(items)
printer = InvoicePrinter()
printer.print_invoice(invoice)
