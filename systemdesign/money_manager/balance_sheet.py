from typing import Dict, List
from systemdesign.money_manager.interface import BalanceSheet


class BalanceSheetSingleton(BalanceSheet):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(BalanceSheetSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.balances = {}
        self.transactions = {}

    def get_user_balance(self, user_id: str) -> float:
        return self.balances.get(user_id, 0.0)

    def get_group_transactions(self, group_id: str) -> List[Dict[str, any]]:
        return self.transactions.get(group_id, [])

    def add_transaction(self, user_id: str, group_id: str, amount: float, description: str, category: str):
        if user_id not in self.balances:
            self.balances[user_id] = 0.0
        self.balances[user_id] += amount
        if group_id not in self.transactions:
            self.transactions[group_id] = []
        self.transactions[group_id].append({
            'user_id': user_id,
            'amount': amount,
            'description': description,
            'category': category
        })
