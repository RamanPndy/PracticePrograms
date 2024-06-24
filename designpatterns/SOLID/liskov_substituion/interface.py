from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def set_width(self, width):
        pass

    @abstractmethod
    def set_height(self, height):
        pass

    @abstractmethod
    def get_area(self):
        pass
