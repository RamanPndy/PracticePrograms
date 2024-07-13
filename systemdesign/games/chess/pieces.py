from systemdesign.games.chess.interface import IPiece

class Piece(IPiece):
    def __init__(self, color: str, position: tuple):
        self._color = color
        self._position = position

    def get_color(self) -> str:
        return self._color

    def get_position(self) -> tuple:
        return self._position

    def set_position(self, position: tuple):
        self._position = position

    def is_valid_move(self, from_position: tuple, to_position: tuple) -> bool:
        raise NotImplementedError("This method should be overridden by subclasses")
    
class King(Piece):
    def is_valid_move(self, from_position: tuple, to_position: tuple) -> bool:
        dx = abs(from_position[0] - to_position[0])
        dy = abs(from_position[1] - to_position[1])
        return max(dx, dy) == 1

class Queen(Piece):
    def is_valid_move(self, from_position: tuple, to_position: tuple) -> bool:
        dx = abs(from_position[0] - to_position[0])
        dy = abs(from_position[1] - to_position[1])
        return dx == dy or from_position[0] == to_position[0] or from_position[1] == to_position[1]

class Rook(Piece):
    def is_valid_move(self, from_position: tuple, to_position: tuple) -> bool:
        return from_position[0] == to_position[0] or from_position[1] == to_position[1]

class Bishop(Piece):
    def is_valid_move(self, from_position: tuple, to_position: tuple) -> bool:
        dx = abs(from_position[0] - to_position[0])
        dy = abs(from_position[1] - to_position[1])
        return dx == dy

class Knight(Piece):
    def is_valid_move(self, from_position: tuple, to_position: tuple) -> bool:
        dx = abs(from_position[0] - to_position[0])
        dy = abs(from_position[1] - to_position[1])
        return (dx, dy) in [(1, 2), (2, 1)]

class Pawn(Piece):
    def is_valid_move(self, from_position: tuple, to_position: tuple) -> bool:
        direction = 1 if self.get_color() == 'white' else -1
        dx = from_position[0] - to_position[0]
        dy = from_position[1] - to_position[1]
        return dx == 0 and dy == direction
