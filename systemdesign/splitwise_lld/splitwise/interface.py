from abc import ABC, abstractmethod

class Expense(ABC):
    @abstractmethod
    def calculate_shares(self):
        pass
