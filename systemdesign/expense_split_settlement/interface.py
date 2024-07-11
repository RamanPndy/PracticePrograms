from abc import ABC, abstractmethod
from systemdesign.expense_split_settlement.models import Expense

class ISettlementService(ABC):
    @abstractmethod
    def calculate_settlements(self, expense: Expense, payees: list) -> dict:
        pass
