class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Lottery:
    def __init__(self, lottery_id, name, draw_date):
        self.lottery_id = lottery_id
        self.name = name
        self.draw_date = draw_date
        self.tickets = []
        self.prizes = []

class Ticket:
    def __init__(self, ticket_id, user, lottery):
        self.ticket_id = ticket_id
        self.user = user
        self.lottery = lottery

class Prize:
    def __init__(self, prize_id, description, amount):
        self.prize_id = prize_id
        self.description = description
        self.amount = amount
