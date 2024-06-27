from systemdesign.splitwise_lld.splitwise.factory import ExpenseFactory, ExpenseType
from systemdesign.splitwise_lld.splitwise.group import Group
from systemdesign.splitwise_lld.splitwise.impl import ExpenseContext
from systemdesign.splitwise_lld.splitwise.users import User
from systemdesign.splitwise_lld.splitwise.notifier import ExpenseNotifier

'''
Define Interfaces
IExpense: Interface for different types of expenses.
IUser: Interface for user-related operations.
IGroup: Interface for group-related operations.
IBalanceSheet: Interface for maintaining balances and settlements.

Implement Design Patterns
Factory Pattern to create expenses.
Observer Pattern for notifying users and balance sheet updates.
Strategy Pattern for different expense types handling.
Composite Pattern for groups and group settlements.
'''

# Create Users
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

# Create a Group
group = Group("group1")
group.add_member(user1)
group.add_member(user2)
group.add_member(user3)

# Create an Equal Expense
expense = ExpenseFactory.create_expense("equal", 300, user1.user_id, users=[user1.user_id, user2.user_id, user3.user_id])
group.add_expense(expense)

# Check Balances
print(group.balance_sheet.get_balance(user1.user_id))
print(group.balance_sheet.get_balance(user2.user_id))
print(group.balance_sheet.get_balance(user3.user_id))