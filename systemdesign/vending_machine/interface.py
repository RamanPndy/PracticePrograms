from abc import ABC, abstractmethod

class IItem(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

class IInventory(ABC):
    @abstractmethod
    def add_item(self, item: IItem, quantity: int):
        pass

    @abstractmethod
    def remove_item(self, item: IItem, quantity: int) -> bool:
        pass

    @abstractmethod
    def get_quantity(self, item: IItem) -> int:
        pass

class IPayment(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class IUserInterface(ABC):
    @abstractmethod
    def select_item(self, item_id: int):
        pass

    @abstractmethod
    def make_payment(self, amount: float):
        pass

    @abstractmethod
    def dispense_item(self, item: IItem):
        pass

class IState(ABC):
    @abstractmethod
    def handle(self):
        pass
