# Initialize the balance sheet and ledger
from systemdesign.money_manager.balance_sheet import BalanceSheetSingleton
from systemdesign.money_manager.factory import ExpenseFactory
from systemdesign.money_manager.repository import InMemoryLedger
from systemdesign.money_manager.service import ExpenseService


balance_sheet = BalanceSheetSingleton()
ledger = InMemoryLedger()

# Create the service
service = ExpenseService(ledger, balance_sheet)

# Add expenses
equal_expense = ExpenseFactory.create_expense('equal', amount=100, user_ids=['user1', 'user2', 'user3'])
service.add_expense(equal_expense, group_id='group1', description='Dinner', category='Food')

exact_expense = ExpenseFactory.create_expense('exact', amounts={'user1': 50, 'user2': 30, 'user3': 20})
service.add_expense(exact_expense, group_id='group1', description='Taxi', category='Transport')

percentage_expense = ExpenseFactory.create_expense('percentage', amount=200, percentages={'user1': 50, 'user2': 30, 'user3': 20})
service.add_expense(percentage_expense, group_id='group1', description='Hotel', category='Accommodation')

# Get user balance
print(balance_sheet.get_user_balance('user1'))

# Get group transactions
print(balance_sheet.get_group_transactions('group1'))
