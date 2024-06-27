from abc import ABC, abstractmethod
from typing import Dict

class IExpense(ABC):
    @abstractmethod
    def calculate_shares(self) -> Dict[str, float]:
        pass

class IUser(ABC):
    @abstractmethod
    def update_balance(self, amount: float):
        pass

class IGroup(ABC):
    @abstractmethod
    def add_expense(self, expense: IExpense):
        pass

    @abstractmethod
    def settle_group(self):
        pass

class IBalanceSheet(ABC):
    @abstractmethod
    def update_balance(self, user_id: str, amount: float):
        pass

    @abstractmethod
    def get_balance(self, user_id: str) -> float:
        pass
