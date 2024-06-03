class Piece:
    def __init__(self, color):
        self.color = color
    
    def is_valid_move(self, start, end, board):
        raise NotImplementedError("This method should be overridden by subclasses")

class King(Piece):
    def is_valid_move(self, start, end, board):
        # King moves one square in any direction
        row_diff = abs(start[0] - end[0])
        col_diff = abs(start[1] - end[1])
        return row_diff <= 1 and col_diff <= 1

class Queen(Piece):
    def is_valid_move(self, start, end, board):
        # Queen moves any number of squares in any direction
        row_diff = abs(start[0] - end[0])
        col_diff = abs(start[1] - end[1])
        return row_diff == col_diff or start[0] == end[0] or start[1] == end[1]

class Rook(Piece):
    def is_valid_move(self, start, end, board):
        # Rook moves any number of squares horizontally or vertically
        return start[0] == end[0] or start[1] == end[1]

class Bishop(Piece):
    def is_valid_move(self, start, end, board):
        # Bishop moves any number of squares diagonally
        row_diff = abs(start[0] - end[0])
        col_diff = abs(start[1] - end[1])
        return row_diff == col_diff

class Knight(Piece):
    def is_valid_move(self, start, end, board):
        # Knight moves in an L-shape: two squares in one direction and one square perpendicular
        row_diff = abs(start[0] - end[0])
        col_diff = abs(start[1] - end[1])
        return (row_diff, col_diff) in [(2, 1), (1, 2)]

class Pawn(Piece):
    def is_valid_move(self, start, end, board):
        # Pawn moves one square forward, captures diagonally
        row_diff = end[0] - start[0]
        col_diff = abs(start[1] - end[1])
        if self.color == 'white':
            return (row_diff == -1 and col_diff == 0 and board[end[0]][end[1]] is None) or \
                   (row_diff == -1 and col_diff == 1 and board[end[0]][end[1]] is not None and board[end[0]][end[1]].color == 'black')
        else:
            return (row_diff == 1 and col_diff == 0 and board[end[0]][end[1]] is None) or \
                   (row_diff == 1 and col_diff == 1 and board[end[0]][end[1]] is not None and board[end[0]][end[1]].color == 'white')

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Setup pieces on the board
        for i in range(8):
            self.board[1][i] = Pawn('black')
            self.board[6][i] = Pawn('white')
        # Rooks
        self.board[0][0] = self.board[0][7] = Rook('black')
        self.board[7][0] = self.board[7][7] = Rook('white')
        # Knights
        self.board[0][1] = self.board[0][6] = Knight('black')
        self.board[7][1] = self.board[7][6] = Knight('white')
        # Bishops
        self.board[0][2] = self.board[0][5] = Bishop('black')
        self.board[7][2] = self.board[7][5] = Bishop('white')
        # Queens
        self.board[0][3] = Queen('black')
        self.board[7][3] = Queen('white')
        # Kings
        self.board[0][4] = King('black')
        self.board[7][4] = King('white')

    def print_board(self):
        for row in self.board:
            print(' '.join([piece.__class__.__name__[0] if piece else '.' for piece in row]))
        print()

    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece and piece.is_valid_move(start, end, self.board):
            self.board[end[0]][end[1]] = piece
            self.board[start[0]][start[1]] = None
            return True
        return False

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'white'
    
    def switch_player(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'

    def play(self):
        while True:
            self.board.print_board()
            print(f"{self.current_player}'s turn")
            try:
                start = tuple(map(int, input("Enter the start position (row col): ").split()))
                end = tuple(map(int, input("Enter the end position (row col): ").split()))
                if self.board.move_piece(start, end):
                    self.switch_player()
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Invalid input, please enter row and column as integers.")

if __name__ == "__main__":
    game = Game()
    game.play()
