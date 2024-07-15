import random

from systemdesign.lottery_system.interface import DrawService, LotteryService, PrizeService, TicketService
from systemdesign.lottery_system.models import Lottery, Ticket

class LotteryServiceImpl(LotteryService):
    def __init__(self):
        self.lotteries = {}

    def create_lottery(self, name, draw_date):
        lottery_id = len(self.lotteries) + 1
        lottery = Lottery(lottery_id, name, draw_date)
        self.lotteries[lottery_id] = lottery
        return lottery

    def get_lottery(self, lottery_id):
        return self.lotteries.get(lottery_id)

class TicketServiceImpl(TicketService):
    def __init__(self):
        self.tickets = []

    def purchase_ticket(self, user, lottery):
        ticket_id = len(self.tickets) + 1
        ticket = Ticket(ticket_id, user, lottery)
        lottery.tickets.append(ticket)
        self.tickets.append(ticket)
        return ticket

    def get_tickets_by_user(self, user):
        return [ticket for ticket in self.tickets if ticket.user == user]

class PrizeServiceImpl(PrizeService):
    def add_prize(self, lottery, prize):
        lottery.prizes.append(prize)

    def get_prizes(self, lottery):
        return lottery.prizes

class DrawServiceImpl(DrawService):
    def perform_draw(self, lottery):
        if not lottery.tickets:
            return None
        winning_ticket = random.choice(lottery.tickets)
        return winning_ticket
