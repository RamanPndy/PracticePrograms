from systemdesign.splitwise_lld.splitwise.interface import IBalanceSheet

class BalanceSheet(IBalanceSheet):
    def __init__(self):
        self.balances = {}

    def update_balance(self, user_id: str, amount: float):
        if user_id in self.balances:
            self.balances[user_id] += amount
        else:
            self.balances[user_id] = amount

    def get_balance(self, user_id: str) -> float:
        return self.balances.get(user_id, 0.0)
