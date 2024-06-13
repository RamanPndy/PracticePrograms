from  abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class CreateDealCommand(Command):
    def __init__(self, deal_manager, item_id, price, quantity, duration):
        self.deal_manager = deal_manager
        self.item_id = item_id
        self.price = price
        self.quantity = quantity
        self.duration = duration

    def execute(self):
        self.deal_manager.create_deal(self.item_id, self.price, self.quantity, self.duration)

class EndDealCommand(Command):
    def __init__(self, deal_manager, deal_id):
        self.deal_manager = deal_manager
        self.deal_id = deal_id

    def execute(self):
        self.deal_manager.end_deal(self.deal_id)

class UpdateDealCommand(Command):
    def __init__(self, deal_manager, deal_id, quantity=None, duration=None):
        self.deal_manager = deal_manager
        self.deal_id = deal_id
        self.quantity = quantity
        self.duration = duration

    def execute(self):
        self.deal_manager.update_deal(self.deal_id, self.quantity, self.duration)

class ClaimDealCommand(Command):
    def __init__(self, deal_manager, user_id, deal_id):
        self.deal_manager = deal_manager
        self.user_id = user_id
        self.deal_id = deal_id

    def execute(self):
        return self.deal_manager.claim_deal(self.user_id, self.deal_id)
