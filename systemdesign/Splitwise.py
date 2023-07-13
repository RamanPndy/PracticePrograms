'''
In this example, we have classes for User, Expense, and ExpenseSplit. The Splitwise class manages the 
users and expenses. Users are represented by the User class, and expenses are represented by the 
Expense class, which includes information about the description, amount, expense type 
(equal, exact, percentage), users involved, and the user who paid the expense. The ExpenseSplit class 
represents the amount split by each user for a particular expense.
The Splitwise class provides methods to add users and expenses. The calculate_balances method 
calculates the balances for each user based on the expenses. The balances are stored in a dictionary, 
where the key is the user ID, and the value is the balance amount.
'''
from enum import Enum

class ExpenseType(Enum):
    EQUAL = 1
    EXACT = 2
    PERCENTAGE = 3

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Expense:
    def __init__(self, expense_id, description, amount, expense_type, users):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.expense_type = expense_type
        self.users = users
        self.paid_by = None
        self.split_by = None

class ExpenseSplit:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount

class Splitwise:
    def __init__(self):
        self.users = {}
        self.expenses = []

    def add_user(self, user_id, name):
        if user_id in self.users:
            raise Exception("User already exists!")
        user = User(user_id, name)
        self.users[user_id] = user

    def add_expense(self, expense_id, description, amount, expense_type, user_splits, paid_by):
        if expense_id in [expense.expense_id for expense in self.expenses]:
            raise Exception("Expense ID already exists!")

        users = []
        total_splits = 0.0

        for user_id, amount in user_splits.items():
            if user_id not in self.users:
                raise Exception("User does not exist!")
            user = self.users[user_id]
            split = ExpenseSplit(user, amount)
            users.append(split)
            total_splits += amount

        if total_splits != amount:
            raise Exception("Invalid split amounts!")

        expense = Expense(expense_id, description, amount, expense_type, users)
        expense.paid_by = self.users[paid_by]
        expense.split_by = expense_type

        self.expenses.append(expense)

    def calculate_balances(self):
        balances = {}

        for expense in self.expenses:
            amount_per_user = expense.amount / len(expense.users)

            for split in expense.users:
                if split.user.user_id not in balances:
                    balances[split.user.user_id] = 0.0

                if expense.split_by == ExpenseType.EQUAL:
                    balances[split.user.user_id] += amount_per_user
                elif expense.split_by == ExpenseType.EXACT:
                    balances[split.user.user_id] += split.amount
                elif expense.split_by == ExpenseType.PERCENTAGE:
                    percentage_share = split.amount / 100
                    balances[split.user.user_id] += expense.amount * percentage_share

            if expense.paid_by.user_id not in balances:
                balances[expense.paid_by.user_id] = 0.0
            balances[expense.paid_by.user_id] -= expense.amount

        return balances

# Usage example
if __name__ == "__main__":
    splitwise = Splitwise()

    # Add users
    splitwise.add_user(1, "Alice")
    splitwise.add_user(2, "Bob")
    splitwise.add_user(3, "Charlie")

    # Add expenses
    user_splits = {1: 100, 2: 100, 3: 100}
    splitwise.add_expense(1, "Dinner", 300, ExpenseType.EQUAL, user_splits, 1)

    user_splits = {1: 200, 3: 100}
    splitwise.add_expense(2, "Movie", 300, ExpenseType.EXACT, user_splits, 2)

    user_splits = {2: 50, 3: 50}
    splitwise.add_expense(3, "Groceries", 100, ExpenseType.PERCENTAGE, user_splits, 3)

    # Calculate balances
    balances = splitwise.calculate_balances()

    # Print balances
    for user_id, balance in balances.items():
        print(f"User {user_id}: {balance}")
