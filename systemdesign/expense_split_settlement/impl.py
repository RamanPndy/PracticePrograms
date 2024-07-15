from systemdesign.expense_split_settlement.interface import ISettlementService
from systemdesign.expense_split_settlement.models import Expense

class EqualSettlementService(ISettlementService):
    def calculate_settlements(self, expense: Expense, payees: list) -> dict:
        total_amount = expense.get_total_amount()
        num_participants = len(expense.get_participants())
        share_per_participant = total_amount / num_participants

        settlements = {}

        for participant in expense.get_participants():
            settlements[participant.name] = 0.0

        for payee in payees:
            amount_paid = payee.amount_paid
            for participant in expense.get_participants():
                settlements[participant.name] += amount_paid / num_participants

        return settlements
