class UserRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserRepository, cls).__new__(cls)
            cls._instance.users = {}
        return cls._instance

    def save(self, user):
        self.users[user.user_id] = user

    def find_by_id(self, user_id):
        return self.users.get(user_id)

class CategoryRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CategoryRepository, cls).__new__(cls)
            cls._instance.categories = {}
        return cls._instance

    def save(self, category):
        self.categories[category.category_id] = category

    def find_by_id(self, category_id):
        return self.categories.get(category_id)

class TransactionRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TransactionRepository, cls).__new__(cls)
            cls._instance.transactions = []
        return cls._instance

    def save(self, transaction):
        self.transactions.append(transaction)

    def find_all_by_user(self, user):
        return [t for t in self.transactions if t.user == user]
