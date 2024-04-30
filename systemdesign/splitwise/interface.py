from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self, message):
        pass

class ExpenseManager(ABC):
    @abstractmethod
    def add_expense(self, payer, amount, participants):
        pass
    
    @abstractmethod
    def settle_expense(self, payer, payee, amount):
        pass
