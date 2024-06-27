# Create Users
from systemdesign.splitwise_lld.splitwise.factory import ExpenseFactory, ExpenseType
from systemdesign.splitwise_lld.splitwise.impl import ExpenseContext
from systemdesign.splitwise_lld.splitwise.interface import User
from systemdesign.splitwise_lld.splitwise.notifier import ExpenseNotifier

'''
Factory Pattern to create expenses.
Observer Pattern for notifying users.
Strategy Pattern for different expense types handling.
'''

user1 = User(1, "Alice")
user2 = User(2, "Bob")
user3 = User(3, "Charlie")

# Add users to notifier
notifier = ExpenseNotifier()
notifier.add_user(user1)
notifier.add_user(user2)
notifier.add_user(user3)

# Create an equal expense
expense = ExpenseFactory.create_expense(ExpenseType.EQUAL, 300, user1, users=[user1, user2, user3])
context = ExpenseContext(expense)
shares = context.calculate_shares()

# Update user balances
for user_id, share in shares.items():
    notifier.notify(user_id, -share)
notifier.notify(user1.user_id, expense.amount)
