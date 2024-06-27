class ExpenseNotifier:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def notify(self, user_id, amount):
        for user in self.users:
            if user.user_id == user_id:
                user.update_balance(amount)
                print(f"User {user.name} balance updated by {amount}. New balance: {user.balance}")
