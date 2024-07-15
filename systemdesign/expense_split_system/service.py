from systemdesign.money_manager.interface import BalanceSheet, Expense, Ledger


class ExpenseService:
    def __init__(self, ledger: Ledger, balance_sheet: BalanceSheet):
        self.ledger = ledger
        self.balance_sheet = balance_sheet

    def add_expense(self, expense: Expense, group_id: str, description: str, category: str) -> None:
        splits = expense.split()
        for user_id, amount in splits.items():
            self.ledger.add_transaction(user_id, amount, description, category)
            self.balance_sheet.add_transaction(user_id, group_id, amount, description, category)
