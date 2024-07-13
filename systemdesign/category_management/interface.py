from abc import ABC, abstractmethod

class ICategoryComponent(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def add(self, component: 'ICategoryComponent'):
        pass

    @abstractmethod
    def remove(self, component: 'ICategoryComponent'):
        pass

    @abstractmethod
    def display(self, indent: int = 0):
        pass

