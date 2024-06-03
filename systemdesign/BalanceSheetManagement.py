'''
Account Management:
'''
class Account:
    '''
    Represents an account with attributes like account ID, name, type (asset, liability, equity), and balance.
    '''
    def __init__(self, account_id, name, account_type):
        self.account_id = account_id
        self.name = name
        self.account_type = account_type
        self.balance = 0

    def update_balance(self, amount):
        self.balance += amount

class AccountManager:
    '''
    Manages the creation and retrieval of accounts.
    '''
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, name, account_type):
        if account_id in self.accounts:
            raise ValueError("Account ID already exists")
        account = Account(account_id, name, account_type)
        self.accounts[account_id] = account
        return account

    def get_account(self, account_id):
        return self.accounts.get(account_id)

'''
Transaction Management:
'''   
from datetime import datetime

class Transaction:
    '''
    Represents a transaction with attributes like transaction ID, date, debit account, credit account, amount, and description.
    '''
    def __init__(self, transaction_id, date, debit_account, credit_account, amount, description):
        self.transaction_id = transaction_id
        self.date = date
        self.debit_account = debit_account
        self.credit_account = credit_account
        self.amount = amount
        self.description = description

class TransactionManager:
    '''
    Manages the creation and processing of transactions.
    '''
    def __init__(self, account_manager):
        self.account_manager = account_manager
        self.transactions = {}

    def create_transaction(self, transaction_id, debit_account_id, credit_account_id, amount, description):
        debit_account = self.account_manager.get_account(debit_account_id)
        credit_account = self.account_manager.get_account(credit_account_id)
        if not debit_account or not credit_account:
            raise ValueError("Invalid account ID")

        transaction = Transaction(transaction_id, datetime.now(), debit_account, credit_account, amount, description)
        self.transactions[transaction_id] = transaction
        self.process_transaction(transaction)
        return transaction

    def process_transaction(self, transaction):
        transaction.debit_account.update_balance(-transaction.amount)
        transaction.credit_account.update_balance(transaction.amount)

'''
Balance Sheet Calculation:
'''
class BalanceSheet:
    '''
    Calculates and stores the balance sheet with sections for assets, liabilities, and equity.
    '''
    def __init__(self, account_manager):
        self.account_manager = account_manager

    def calculate_balance_sheet(self):
        assets = []
        liabilities = []
        equity = []

        for account in self.account_manager.accounts.values():
            if account.account_type == "asset":
                assets.append(account)
            elif account.account_type == "liability":
                liabilities.append(account)
            elif account.account_type == "equity":
                equity.append(account)

        return {
            "assets": assets,
            "liabilities": liabilities,
            "equity": equity
        }

    def print_balance_sheet(self, balance_sheet):
        print("Balance Sheet:")
        print("Assets:")
        for account in balance_sheet['assets']:
            print(f"{account.name}: {account.balance}")

        print("Liabilities:")
        for account in balance_sheet['liabilities']:
            print(f"{account.name}: {account.balance}")

        print("Equity:")
        for account in balance_sheet['equity']:
            print(f"{account.name}: {account.balance}")

        total_assets = sum(account.balance for account in balance_sheet['assets'])
        total_liabilities = sum(account.balance for account in balance_sheet['liabilities'])
        total_equity = sum(account.balance for account in balance_sheet['equity'])

        print(f"Total Assets: {total_assets}")
        print(f"Total Liabilities: {total_liabilities}")
        print(f"Total Equity: {total_equity}")
        print(f"Assets = Liabilities + Equity: {total_assets == total_liabilities + total_equity}")

'''
Reporting:
'''
class ReportGenerator:
    '''
    Generates and prints reports for the balance sheet and transactions.
    '''
    def __init__(self, balance_sheet, transaction_manager):
        self.balance_sheet = balance_sheet
        self.transaction_manager = transaction_manager

    def generate_balance_sheet_report(self):
        balance_sheet = self.balance_sheet.calculate_balance_sheet()
        self.balance_sheet.print_balance_sheet(balance_sheet)

    def generate_transaction_report(self):
        print("Transaction Report:")
        for transaction in self.transaction_manager.transactions.values():
            print(f"ID: {transaction.transaction_id}, Date: {transaction.date}, "
                  f"Debit: {transaction.debit_account.name}, Credit: {transaction.credit_account.name}, "
                  f"Amount: {transaction.amount}, Description: {transaction.description}")

# Initialize managers
account_manager = AccountManager()
transaction_manager = TransactionManager(account_manager)
balance_sheet = BalanceSheet(account_manager)
report_generator = ReportGenerator(balance_sheet, transaction_manager)

# Create accounts
cash_account = account_manager.create_account(1, "Cash", "asset")
accounts_payable = account_manager.create_account(2, "Accounts Payable", "liability")
owners_equity = account_manager.create_account(3, "Owner's Equity", "equity")

# Create transactions
transaction_manager.create_transaction(1, 1, 2, 1000, "Purchase of supplies")
transaction_manager.create_transaction(2, 3, 1, 5000, "Initial capital investment")

# Generate reports
report_generator.generate_balance_sheet_report()
report_generator.generate_transaction_report()
