class Participant:
    def __init__(self, participant_id: int, name: str):
        self.participant_id = participant_id
        self.name = name

class Payee:
    def __init__(self, payee_id: int, name: str, amount_paid: float):
        self.payee_id = payee_id
        self.name = name
        self.amount_paid = amount_paid

class Expense:
    def __init__(self, total_amount: float, participants: list):
        self.total_amount = total_amount
        self.participants = participants  # List of Participant objects

    def get_total_amount(self):
        return self.total_amount

    def get_participants(self):
        return self.participants
