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
    def move(self, component: 'ICategoryComponent', new_parent: 'ICategoryComponent'):
        pass

    @abstractmethod
    def get_hierarchy(self) -> str:
        pass
