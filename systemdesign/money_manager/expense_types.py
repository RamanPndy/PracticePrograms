from typing import Dict, List

from systemdesign.money_manager.interface import Expense


class EqualExpense(Expense):
    def __init__(self, amount: float, user_ids: List[str]):
        self.amount = amount
        self.user_ids = user_ids

    def split(self) -> Dict[str, float]:
        split_amount = self.amount / len(self.user_ids)
        return {user_id: split_amount for user_id in self.user_ids}

class ExactExpense(Expense):
    def __init__(self, amounts: Dict[str, float]):
        self.amounts = amounts

    def split(self) -> Dict[str, float]:
        return self.amounts

class PercentageExpense(Expense):
    def __init__(self, amount: float, percentages: Dict[str, float]):
        self.amount = amount
        self.percentages = percentages

    def split(self) -> Dict[str, float]:
        return {user_id: self.amount * percentage / 100 for user_id, percentage in self.percentages.items()}
