from collections import defaultdict
from datetime import datetime

from systemdesign.money_manager.interface import AnalyticsService, CategoryService, TransactionService, UserService
from systemdesign.money_manager.models import Category, Transaction, User

class UserServiceImpl(UserService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserServiceImpl, cls).__new__(cls)
            cls._instance.users = {}
        return cls._instance

    def create_user(self, name, email):
        user_id = len(self.users) + 1
        user = User(user_id, name, email)
        self.users[user_id] = user
        return user

    def get_user(self, user_id):
        return self.users.get(user_id)

class CategoryServiceImpl(CategoryService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CategoryServiceImpl, cls).__new__(cls)
            cls._instance.categories = {}
        return cls._instance

    def create_category(self, user, name):
        category_id = len(self.categories) + 1
        category = Category(category_id, name, user)
        self.categories[category_id] = category
        user.categories.append(category)
        return category

    def get_category(self, category_id):
        return self.categories.get(category_id)

class TransactionServiceImpl(TransactionService):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TransactionServiceImpl, cls).__new__(cls)
            cls._instance.transactions = []
        return cls._instance

    def record_transaction(self, user, category, amount, date):
        transaction_id = len(self.transactions) + 1
        transaction = Transaction(transaction_id, user, category, amount, date)
        self.transactions.append(transaction)
        return transaction

    def get_transactions(self, user):
        return [t for t in self.transactions if t.user == user]

class AnalyticsServiceImpl(AnalyticsService):
    def get_spend_analytics(self, user, period):
        transactions = TransactionServiceImpl().get_transactions(user)
        analytics = defaultdict(float)
        for transaction in transactions:
            if period == 'monthly' and transaction.date.month == datetime.now().month:
                analytics[transaction.category.name] += transaction.amount
            elif period == 'annually' and transaction.date.year == datetime.now().year:
                analytics[transaction.category.name] += transaction.amount
        return analytics
