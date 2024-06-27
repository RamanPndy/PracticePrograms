from systemdesign.splitwise_lld.splitwise.balance_sheet import BalanceSheet
from systemdesign.splitwise_lld.splitwise.interface import IExpense, IGroup, IUser

class Group(IGroup):
    def __init__(self, group_id: str):
        self.group_id = group_id
        self.members = []
        self.expenses = []
        self.balance_sheet = BalanceSheet()

    def add_member(self, user: IUser):
        self.members.append(user)

    def add_expense(self, expense: IExpense):
        self.expenses.append(expense)
        shares = expense.calculate_shares()
        for user_id, share in shares.items():
            self.balance_sheet.update_balance(user_id, -share)
        self.balance_sheet.update_balance(expense.paid_by, expense.amount)

    def settle_group(self):
        # Settlement logic here
        pass
