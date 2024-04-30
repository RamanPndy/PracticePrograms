class Splitwise(Subject, ExpenseManager):
    def __init__(self):
        self.users = []
        self.expenses = []
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def add_user(self, user):
        self.users.append(user)

    def add_expense(self, payer, amount, participants):
        self.expenses.append({
            'payer': payer,
            'amount': amount,
            'participants': participants
        })
        total_participants = len(participants)
        share = amount / total_participants
        payer.pay(amount)
        payer_message = f"You paid ${amount} for {total_participants} participants."
        payer.receive(amount - share * (total_participants - 1))
        for participant in participants:
            if participant != payer:
                participant.receive(share)
                self.notify(f"{payer.name} paid ${share} for {participant.name}")

    def settle_expense(self, payer, payee, amount):
        if payer.get_balance() >= amount:
            payer.pay(amount)
            payee.receive(amount)
            self.notify(f"{payer.name} settled ${amount} with {payee.name}")
        else:
            print("Insufficient balance to settle the expense.")
