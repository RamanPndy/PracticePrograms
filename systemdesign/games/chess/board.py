from systemdesign.games.chess.interface import IBoard, IPiece
from systemdesign.games.chess.pieces import Bishop, King, Knight, Pawn, Queen, Rook

class Board(IBoard):
    def __init__(self):
        self._board = [[None for _ in range(8)] for _ in range(8)]
        self.setup()

    def setup(self):
        # Setup the pieces on the board
        self._board[0][0] = Rook('black', (0, 0))
        self._board[0][1] = Knight('black', (0, 1))
        self._board[0][2] = Bishop('black', (0, 2))
        self._board[0][3] = Queen('black', (0, 3))
        self._board[0][4] = King('black', (0, 4))
        self._board[0][5] = Bishop('black', (0, 5))
        self._board[0][6] = Knight('black', (0, 6))
        self._board[0][7] = Rook('black', (0, 7))
        for i in range(8):
            self._board[1][i] = Pawn('black', (1, i))

        self._board[7][0] = Rook('white', (7, 0))
        self._board[7][1] = Knight('white', (7, 1))
        self._board[7][2] = Bishop('white', (7, 2))
        self._board[7][3] = Queen('white', (7, 3))
        self._board[7][4] = King('white', (7, 4))
        self._board[7][5] = Bishop('white', (7, 5))
        self._board[7][6] = Knight('white', (7, 6))
        self._board[7][7] = Rook('white', (7, 7))
        for i in range(8):
            self._board[6][i] = Pawn('white', (6, i))

    def move_piece(self, from_position: tuple, to_position: tuple) -> bool:
        piece = self.get_piece_at(from_position)
        if piece and piece.is_valid_move(from_position, to_position):
            self._board[to_position[0]][to_position[1]] = piece
            self._board[from_position[0]][from_position[1]] = None
            piece.set_position(to_position)
            return True
        return False

    def get_piece_at(self, position: tuple) -> IPiece:
        return self._board[position[0]][position[1]]
