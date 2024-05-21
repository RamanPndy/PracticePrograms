from systemdesign.splitwise.users import User
from systemdesign.splitwise.expensemanager import Splitwise

# Create users and Splitwise instance
alice = User("Alice")
bob = User("Bob")
charlie = User("Charlie")

splitwise = Splitwise()
splitwise.add_user(alice)
splitwise.add_user(bob)
splitwise.add_user(charlie)

# Attach users to observer list
splitwise.attach(alice)
splitwise.attach(bob)
splitwise.attach(charlie)

# Adding expenses and settling balances
splitwise.add_expense(alice, 100, [alice, bob, charlie])
splitwise.add_expense(bob, 50, [bob, charlie])
splitwise.settle_expense(alice, charlie, 30)

print(f"Alice's Balance: ${alice.get_balance()}")
print(f"Bob's Balance: ${bob.get_balance()}")
print(f"Charlie's Balance: ${charlie.get_balance()}")
