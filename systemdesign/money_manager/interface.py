from abc import ABC, abstractmethod
from typing import List, Dict

class Expense(ABC):
    @abstractmethod
    def split(self) -> Dict[str, float]:
        pass

class Ledger(ABC):
    @abstractmethod
    def add_transaction(self, user_id: str, amount: float, description: str, category: str) -> None:
        pass

class BalanceSheet(ABC):
    @abstractmethod
    def get_user_balance(self, user_id: str) -> float:
        pass

    @abstractmethod
    def get_group_transactions(self, group_id: str) -> List[Dict[str, any]]:
        pass
