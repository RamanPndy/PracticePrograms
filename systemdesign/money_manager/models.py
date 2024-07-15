class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.categories = []

class Category:
    def __init__(self, category_id, name, user):
        self.category_id = category_id
        self.name = name
        self.user = user

class Transaction:
    def __init__(self, transaction_id, user, category, amount, date):
        self.transaction_id = transaction_id
        self.user = user
        self.category = category
        self.amount = amount
        self.date = date

class Ledger:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
