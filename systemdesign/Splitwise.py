class SplitType:
    EQUAL = 1
    UNEQUAL = 2
    PERCENTAGE = 3

class Split:
    def __init__(self, user, amount, percentage) -> None:
        self.user = user
        self.amount = amount
        self.percentage = percentage
        
class Expense:
    def __init__(self, id, description, amount, paidByUser, splitType, splitDetaills) -> None:
        self.id = id
        self.description = description
        self.amount = amount
        self.paidByUser = paidByUser
        self.splitType = splitType
        self.splitDetaills = list()
        self.splitDetaills.extend(splitDetaills)

# Expense has Split
# Expense has User

class BalanceSheetController:
    def updateUserExpenseBalanceSheet(self, expensePaidBy, splits, totalExpenseAmount):
        expensePaidBy.userExpenseBalanceSheet.totalPayment += totalExpenseAmount
        for split in splits:
            oweUserExpenseBalanceSheet = split.user.userExpenseBalanceSheet
            oweAmount = split.amount
            if expensePaidBy.id == split.user.id:
                 expensePaidBy.userExpenseBalanceSheet.totalYourExpense += oweAmount
            else:
                # update the balance of paid user
                expensePaidBy.userExpenseBalanceSheet.totalYouGetBack += oweAmount
                userOweBalance = Balance()
                if split.user.id not in expensePaidBy.userExpenseBalanceSheet.userVsBalance:
                    expensePaidBy.userExpenseBalanceSheet.userVsBalance[split.user.id] = userOweBalance
                else:
                    userOweBalance = expensePaidBy.userExpenseBalanceSheet.userVsBalance[split.user.id]
                userOweBalance.amountGetBack += oweAmount

                # update the balance sheet of owe user
                oweUserExpenseBalanceSheet.totalYouOwe += oweAmount
                oweUserExpenseBalanceSheet.totalYourExpense += oweAmount

                userPaidBalance = Balance()
                if expensePaidBy.id not in expensePaidBy.userExpenseBalanceSheet.userVsBalance:
                    expensePaidBy.userExpenseBalanceSheet.userVsBalance[expensePaidBy.id] = userPaidBalance
                else:
                    userPaidBalance = expensePaidBy.userExpenseBalanceSheet.userVsBalance[expensePaidBy.id]
                userPaidBalance.amountOwe += oweAmount

class ExpenseController:
    def __init__(self) -> None:
        self.balanceSheetController = BalanceSheetController()

    def createExpense(self, expenseId, description, expenseAmount, spiltDetails, splitType, paidByUser):
        expenseSplit = SplitFactory.getSplitObject(splitType)
        expenseSplit.validateSplitRequest(spiltDetails, expenseAmount)
        expense = Expense(expenseId, description, expenseAmount, paidByUser, splitType, spiltDetails)
        self.balanceSheetController.updateUserExpenseBalanceSheet(paidByUser, spiltDetails, expenseAmount)
        return expense

class ExpenseSplitInterface:
    def validateSplitRequest(splitList, totalAmount):
        pass

class EqualExpenseSplit(ExpenseSplitInterface):
    pass

class UnEqualExpenseSplit(ExpenseSplitInterface):
    pass

class PercentageExpenseSplit(ExpenseSplitInterface):
    pass

class SplitFactory():
    def getSplitObject(splitType):
        if splitType == SplitType.EQUAL:
            return EqualExpenseSplit()
        elif splitType == SplitType.UNEQUAL:
            return UnEqualExpenseSplit()
        elif splitType == SplitType.PERCENTAGE:
            return PercentageExpenseSplit()

# Each User has peer expense balance sheet
class User:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.userExpenseBalanceSheet = UserExpenseBalanceSheet()

class Balance:
    def __init__(self) -> None:
        self.amountOwe = 0
        self.amountGetBack = 0

class UserExpenseBalanceSheet:
    def __init__(self) -> None:
        self.userVsBalance = dict()
        self.totalPayment = 0
        self.totalYouOwe = 0
        self.totalYouGetBack = 0
        self.totalYourExpense = 0

#UserController has list of Users
class UserController:
    def __init__(self, users) -> None:
        self.users = users

    # user CRUD operations

class Group:
    def __init__(self, id, name, users) -> None:
        self.id = id
        self.name = name
        self.groupMembers = users
        self.expenseList = list()
        self.expenseController = ExpenseController()

#GroupController has list of Groups
class GroupController:
    def __init__(self, groups) -> None:
        self.groups = groups

#Splitwise has UserController
class SplitWise:
    def __init__(self) -> None:
        self.userController = UserController()
        self.groupController = GroupController()