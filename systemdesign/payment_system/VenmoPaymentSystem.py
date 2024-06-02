import time
'''
Components
User: Represents a user in the system with an account balance.
Transaction: Represents a money transfer between users.
Wallet: Manages the user's balance and transactions.
PaymentSystem: Manages users, wallets, and transactions.
'''
# Step 1: Define the User
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.email})"
    
# Step 2: Define the Wallet
class Wallet:
    def __init__(self, user):
        self.user = user
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('deposit', amount))
        print(f"Deposited ${amount} to {self.user.name}'s wallet. New balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(('withdraw', amount))
            print(f"Withdrew ${amount} from {self.user.name}'s wallet. New balance: ${self.balance}")
        else:
            print(f"Insufficient funds in {self.user.name}'s wallet. Current balance: ${self.balance}")

    def __repr__(self):
        return f"Wallet({self.user}, Balance: ${self.balance})"

# Step 3: Define the Transaction
class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()

    def __repr__(self):
        return f"Transaction(from: {self.sender.user.name}, to: {self.recipient.user.name}, amount: ${self.amount}, timestamp: {self.timestamp})"
    
# Step 4: Define the PaymentSystem
class PaymentSystem:
    def __init__(self):
        self.users = {}
        self.wallets = {}

    def create_user(self, user_id, name, email):
        user = User(user_id, name, email)
        wallet = Wallet(user)
        self.users[user_id] = user
        self.wallets[user_id] = wallet
        print(f"Created user {name} with email {email}")
        return user

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def get_wallet(self, user_id):
        return self.wallets.get(user_id, None)

    def deposit_to_wallet(self, user_id, amount):
        wallet = self.get_wallet(user_id)
        if wallet:
            wallet.deposit(amount)
        else:
            print(f"Wallet for user_id {user_id} not found")

    def transfer(self, sender_id, recipient_id, amount):
        sender_wallet = self.get_wallet(sender_id)
        recipient_wallet = self.get_wallet(recipient_id)

        if sender_wallet and recipient_wallet:
            if sender_wallet.balance >= amount:
                sender_wallet.withdraw(amount)
                recipient_wallet.deposit(amount)
                transaction = Transaction(sender_wallet, recipient_wallet, amount)
                sender_wallet.transactions.append(transaction)
                recipient_wallet.transactions.append(transaction)
                print(f"Transfer of ${amount} from {sender_wallet.user.name} to {recipient_wallet.user.name} successful")
            else:
                print(f"Insufficient funds in {sender_wallet.user.name}'s wallet for transfer")
        else:
            print(f"Sender or recipient wallet not found")

# Initialize the payment system
payment_system = PaymentSystem()

# Create users
user1 = payment_system.create_user(1, "Alice", "alice@example.com")
user2 = payment_system.create_user(2, "Bob", "bob@example.com")

# Deposit money into user wallets
payment_system.deposit_to_wallet(user1.user_id, 100)
payment_system.deposit_to_wallet(user2.user_id, 50)

# Transfer money between users
payment_system.transfer(user1.user_id, user2.user_id, 30)

# Check balances
wallet1 = payment_system.get_wallet(user1.user_id)
wallet2 = payment_system.get_wallet(user2.user_id)
print(wallet1)
print(wallet2)


