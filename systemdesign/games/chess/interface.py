from abc import ABC, abstractmethod

class IBoard(ABC):
    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def move_piece(self, from_position: tuple, to_position: tuple) -> bool:
        pass

    @abstractmethod
    def get_piece_at(self, position: tuple) -> 'IPiece':
        pass

class IPiece(ABC):
    @abstractmethod
    def get_color(self) -> str:
        pass

    @abstractmethod
    def get_position(self) -> tuple:
        pass

    @abstractmethod
    def set_position(self, position: tuple):
        pass

    @abstractmethod
    def is_valid_move(self, from_position: tuple, to_position: tuple) -> bool:
        pass
