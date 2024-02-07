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
from collections import defaultdict

class ExpenseType(Enum):
    EQUAL = 1
    EXACT = 2
    PERCENTAGE = 3

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Group:
    def __init__(self, group_id, name, members):
        self.group_id = group_id
        self.name = name
        self.members = members  # List of users in the group
        self.expenses = []  # List to store group expenses

    def add_expense(self, expense):
        self.expenses.append(expense)

class Expense:
    def __init__(self, expense_id, description, amount, expense_type, users):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.expense_type = expense_type
        self.users = users
        self.paid_by = None
        self.split_by = None
    
    def __init__(self, expense_id, payer, amount, participants, expense_type):
        self.expense_id = expense_id
        self.payer = payer
        self.amount = amount
        self.participants = participants
        self.expense_type = expense_type

class ExpenseSplit:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount

class Splitwise:
    def __init__(self):
        self.users = {}
        self.expenses = []
        self.groups = {}
        self.balance_sheet = defaultdict(float)

    def add_user(self, user_id, name):
        if user_id in self.users:
            raise Exception("User already exists!")
        user = User(user_id, name)
        self.users[user_id] = user
    
    def create_group(self, group_id, name, member_ids):
        members = [self.users[user_id] for user_id in member_ids if user_id in self.users]
        if members:
            self.groups[group_id] = Group(group_id, name, members)

    def add_expense_to_group(self, group_id, payer_id, amount, participant_ids):
        if group_id in self.groups and payer_id in self.users:
            payer = self.users[payer_id]
            participants = [self.users[user_id] for user_id in participant_ids if user_id in self.users]
            expense = Expense(payer, amount, participants)
            self.groups[group_id].add_expense(expense)

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
    
    def add_expense(self, expense_id, payer_id, amount, participants, expense_type):
        payer = self.users.get(payer_id)
        if payer is None:
            print("Payer does not exist.")
            return

        expense = Expense(expense_id, payer, amount, participants, expense_type)
        self.expenses.append(expense)

        if expense.expense_type == ExpenseType.EQUAL:
            self.split_equal(expense)
        elif expense.expense_type == ExpenseType.EXACT:
            self.split_exact(expense)
        elif expense.expense_type == ExpenseType.PERCENT:
            self.split_percent(expense)

    def split_equal(self, expense):
        num_participants = len(expense.participants)
        if num_participants == 0:
            return

        share = expense.amount / num_participants
        for participant_id in expense.participants:
            self.balance_sheet[(participant_id, expense.payer.user_id)] += share
            self.balance_sheet[(expense.payer.user_id, participant_id)] -= share

    def split_exact(self, expense):
        for participant_id, exact_amount in expense.participants.items():
            self.balance_sheet[(participant_id, expense.payer.user_id)] += exact_amount
            self.balance_sheet[(expense.payer.user_id, participant_id)] -= exact_amount

    def split_percent(self, expense):
        for participant_id, percent in expense.participants.items():
            amount = expense.amount * percent / 100
            self.balance_sheet[(participant_id, expense.payer.user_id)] += amount
            self.balance_sheet[(expense.payer.user_id, participant_id)] -= amount

    def print_balance(self):
        for (user1, user2), amount in self.balance_sheet.items():
            if amount != 0:
                print(f"{self.users[user1].name} owes {self.users[user2].name}: {amount}")
    
    def settle_expenses(self):
        balances = defaultdict(int)

        for expense in self.expenses:
            amount_per_person = 0
            if expense.expense_type == ExpenseType.EQUAL:
                amount_per_person = expense.amount / len(expense.participants)
            elif expense.expense_type == ExpenseType.UNEQUAL:
                amount_per_person = expense.amount
            elif expense.expense_type == ExpenseType.PERCENTAGE:
                total_percentage = sum(expense.percentages.values())
                for participant in expense.participants:
                    amount_per_person += expense.amount * (expense.percentages.get(participant.user_id, 0) / total_percentage)

            for participant in expense.participants:
                balances[participant.user_id] += amount_per_person

            balances[expense.payer.user_id] -= expense.amount

        # Print balances
        for user_id, balance in balances.items():
            print(f"User {self.users[user_id].name}: Balance {balance}")


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

    splitwise.create_group(1, "Friends", [1, 2, 3])

    # Add an expense to the group
    splitwise.add_expense_to_group(1, 1, 100, [1, 2])

    # Calculate balances
    balances = splitwise.calculate_balances()

    # Print balances
    for user_id, balance in balances.items():
        print(f"User {user_id}: {balance}")
