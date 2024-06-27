from systemdesign.splitwise_lld.splitwise.interface import IUser

class User(IUser):
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.balance = 0.0

    def update_balance(self, amount: float):
        self.balance += amount
        print(f"{self.name}'s balance updated by {amount}. New balance: {self.balance}")