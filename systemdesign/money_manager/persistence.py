from systemdesign.money_manager.interface import Ledger


class InMemoryLedger(Ledger):
    def __init__(self):
        self.transactions = []

    def add_transaction(self, user_id: str, amount: float, description: str, category: str) -> None:
        self.transactions.append({
            'user_id': user_id,
            'amount': amount,
            'description': description,
            'category': category
        })
