from abc import ABC, abstractmethod

class LotteryService(ABC):
    @abstractmethod
    def create_lottery(self, name, draw_date):
        pass

    @abstractmethod
    def get_lottery(self, lottery_id):
        pass

class TicketService(ABC):
    @abstractmethod
    def purchase_ticket(self, user, lottery):
        pass

    @abstractmethod
    def get_tickets_by_user(self, user):
        pass

class PrizeService(ABC):
    @abstractmethod
    def add_prize(self, lottery, prize):
        pass

    @abstractmethod
    def get_prizes(self, lottery):
        pass

class DrawService(ABC):
    @abstractmethod
    def perform_draw(self, lottery):
        pass
