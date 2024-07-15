from abc import ABC, abstractmethod

class UserService(ABC):
    @abstractmethod
    def create_user(self, name, email):
        pass

    @abstractmethod
    def get_user(self, user_id):
        pass

class CategoryService(ABC):
    @abstractmethod
    def create_category(self, user, name):
        pass

    @abstractmethod
    def get_category(self, category_id):
        pass

class TransactionService(ABC):
    @abstractmethod
    def record_transaction(self, user, category, amount, date):
        pass

    @abstractmethod
    def get_transactions(self, user):
        pass

class AnalyticsService(ABC):
    @abstractmethod
    def get_spend_analytics(self, user, period):
        pass
