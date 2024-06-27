from systemdesign.splitwise_lld.splitwise.interface import Expense

class ExactExpense(Expense):
    def __init__(self, amount, paid_by, splits):
        self.amount = amount
        self.paid_by = paid_by
        self.splits = splits

    def calculate_shares(self):
        return self.splits

class EqualExpense(Expense):
    def __init__(self, amount, paid_by, users):
        self.amount = amount
        self.paid_by = paid_by
        self.users = users

    def calculate_shares(self):
        share = self.amount / len(self.users)
        return {user.user_id: share for user in self.users}

class PercentageExpense(Expense):
    def __init__(self, amount, paid_by, splits):
        self.amount = amount
        self.paid_by = paid_by
        self.splits = splits

    def calculate_shares(self):
        return {user.user_id: self.amount * percentage / 100 for user, percentage in self.splits.items()}

class ExpenseContext:
    def __init__(self, expense_type: Expense):
        self.expense_type = expense_type

    def calculate_shares(self):
        return self.expense_type.calculate_shares()
