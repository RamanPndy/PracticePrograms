from systemdesign.games.chess.board import Board

class Game:
    def __init__(self):
        self._board = Board()
        self._current_turn = 'white'

    def move(self, from_position: tuple, to_position: tuple) -> bool:
        piece = self._board.get_piece_at(from_position)
        if piece and piece.get_color() == self._current_turn:
            if self._board.move_piece(from_position, to_position):
                self._current_turn = 'black' if self._current_turn == 'white' else 'white'
                return True
        return False

    def display_board(self):
        for row in self._board._board:
            print(' '.join([str(piece) if piece else ' . ' for piece in row]))
