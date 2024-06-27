from enum import Enum
from systemdesign.splitwise_lld.splitwise.impl import EqualExpense, ExactExpense, PercentageExpense

class ExpenseType(Enum):
    EQUAL, EXACT, PERCENTAGE = 1, 2, 3

class ExpenseFactory:
    @staticmethod
    def create_expense(expense_type, amount, paid_by, splits=None, users=None):
        if expense_type == ExpenseType.EXACT:
            return ExactExpense(amount, paid_by, splits)
        elif expense_type == ExpenseType.EQUAL:
            return EqualExpense(amount, paid_by, users)
        elif expense_type == ExpenseType.PERCENTAGE:
            return PercentageExpense(amount, paid_by, splits)
        else:
            raise ValueError("Unknown expense type")
