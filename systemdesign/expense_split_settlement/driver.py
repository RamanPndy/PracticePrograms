# Create participants
from systemdesign.expense_split_settlement.impl import EqualSettlementService
from systemdesign.expense_split_settlement.models import Expense, Participant, Payee


participant1 = Participant(participant_id=1, name="Alice")
participant2 = Participant(participant_id=2, name="Bob")
participant3 = Participant(participant_id=3, name="Charlie")
participants = [participant1, participant2, participant3]

# Create payees
payee1 = Payee(payee_id=1, name="David", amount_paid=120)
payee2 = Payee(payee_id=2, name="Eve", amount_paid=230)
payee3 = Payee(payee_id=3, name="Frank", amount_paid=150)
payees = [payee1, payee2, payee3]

# Create expense
expense = Expense(total_amount=500, participants=participants)

# Calculate settlements
settlement_service = EqualSettlementService()
settlements = settlement_service.calculate_settlements(expense, payees)

# Print settlements
for participant, amount in settlements.items():
    print(f"{participant}: {amount}")
