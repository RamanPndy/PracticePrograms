import uuid
from datetime import datetime

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.wallet = 0  # User's wallet balance

class Transaction:
    def __init__(self, transaction_id, sender_id, receiver_id, amount, timestamp):
        self.transaction_id = transaction_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.amount = amount
        self.timestamp = timestamp

class PaymentGateway:
    def __init__(self):
        self.users = {}  # Dictionary to store users (user_id: User)
        self.accounts = {}  # Dictionary to store user accounts (user_id: account_balance)
        self.transactions = {}  # Dictionary to store transactions (transaction_id: transaction_details)

    def register_user(self, name, email, password):
        user_id = uuid.uuid4().hex
        user = User(user_id, name, email, password)
        self.users[user_id] = user
        return user_id

    def login_user(self, email, password):
        for user_id, user in self.users.items():
            if user.email == email and user.password == password:
                return user_id
        return None

    def deposit_money(self, user_id, amount):
        if user_id in self.users:
            self.users[user_id].wallet += amount
            return True
        return False

    def withdraw_money(self, user_id, amount):
        if user_id in self.users and self.users[user_id].wallet >= amount:
            self.users[user_id].wallet -= amount
            return True
        return False

    def transfer_money(self, sender_id, receiver_id, amount):
        if sender_id in self.users and receiver_id in self.users:
            sender = self.users[sender_id]
            receiver = self.users[receiver_id]
            if sender.wallet >= amount:
                sender.wallet -= amount
                receiver.wallet += amount
                transaction_id = uuid.uuid4().hex
                timestamp = datetime.now()
                transaction = Transaction(transaction_id, sender_id, receiver_id, amount, timestamp)
                self.transactions.append(transaction)
                return True, transaction_id
        return False, None
    
    def create_account(self, user_id, initial_balance=0):
        if user_id not in self.accounts:
            self.accounts[user_id] = initial_balance

    def deposit(self, user_id, amount):
        if user_id in self.accounts:
            self.accounts[user_id] += amount
            transaction_id = uuid.uuid4().hex
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.transactions[transaction_id] = {'type': 'Deposit', 'user_id': user_id, 'amount': amount, 'timestamp': timestamp}
            return transaction_id
        else:
            return None

    def withdraw(self, user_id, amount):
        if user_id in self.accounts and self.accounts[user_id] >= amount:
            self.accounts[user_id] -= amount
            transaction_id = uuid.uuid4().hex
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.transactions[transaction_id] = {'type': 'Withdrawal', 'user_id': user_id, 'amount': amount, 'timestamp': timestamp}
            return transaction_id
        else:
            return None

    def transfer(self, sender_id, receiver_id, amount):
        if sender_id in self.accounts and receiver_id in self.accounts and self.accounts[sender_id] >= amount:
            self.accounts[sender_id] -= amount
            self.accounts[receiver_id] += amount
            transaction_id = uuid.uuid4().hex
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.transactions[transaction_id] = {'type': 'Transfer', 'sender_id': sender_id, 'receiver_id': receiver_id, 'amount': amount, 'timestamp': timestamp}
            return transaction_id
        else:
            return None

    def get_balance(self, user_id):
        return self.accounts.get(user_id, None)

    def get_transaction_details(self, transaction_id):
        return self.transactions.get(transaction_id, None)

# Example usage:
payment_gateway = PaymentGateway()

# Register users
user1_id = payment_gateway.register_user("Alice", "alice@example.com", "password1")
user2_id = payment_gateway.register_user("Bob", "bob@example.com", "password2")

# Deposit money
payment_gateway.deposit_money(user1_id, 100)
payment_gateway.deposit_money(user2_id, 50)

# Transfer money
success, transaction_id = payment_gateway.transfer_money(user1_id, user2_id, 30)
if success:
    print(f"Transaction successful! Transaction ID: {transaction_id}")
else:
    print("Transaction failed.")

# Check wallet balances
print(f"Alice's balance: {payment_gateway.users[user1_id].wallet}")
print(f"Bob's balance: {payment_gateway.users[user2_id].wallet}")
