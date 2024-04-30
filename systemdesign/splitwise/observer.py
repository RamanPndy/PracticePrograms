class User(Observer):
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def update(self, message):
        print(f"{self.name} received: {message}")

    def pay(self, amount):
        self.balance -= amount

    def receive(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance
