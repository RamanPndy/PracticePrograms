from abc import ABC, abstractmethod

class Cell(ABC):
    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set_value(self, value):
        pass

    @abstractmethod
    def add_dependency(self, cell):
        pass

    @abstractmethod
    def remove_dependency(self, cell):
        pass

    @abstractmethod
    def notify_dependents(self):
        pass

class Sheet(ABC):
    @abstractmethod
    def get_cell(self, row, col):
        pass

    @abstractmethod
    def set_cell(self, row, col, value):
        pass

    @abstractmethod
    def evaluate(self):
        pass
