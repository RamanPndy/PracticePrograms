from systemdesign.money_manager.interface import Expense
from systemdesign.splitwise_lld.splitwise.impl import EqualExpense, ExactExpense, PercentageExpense


class ExpenseFactory:
    @staticmethod
    def create_expense(expense_type: str, **kwargs) -> Expense:
        if expense_type == 'equal':
            return EqualExpense(**kwargs)
        elif expense_type == 'exact':
            return ExactExpense(**kwargs)
        elif expense_type == 'percentage':
            return PercentageExpense(**kwargs)
        else:
            raise ValueError("Unknown expense type")
