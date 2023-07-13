class State:
    FIRST = 1
    SECOND = 2
    DRAW = 3
    UNDECIDED = 4

class Move:
    def __init__(self,player, row, col) -> None:
        self.player = player
        self.row = row
        self.col = col

class Board:
    def initialize():
        pass
    def getBoard():
        pass
    def getWinner():
        pass
    def getCurrentPlayer():
        pass
    def makeMove(move):
        pass

class Game:
    def __init__(self,id,p1,p2) -> None:
        self.id = id
        self.player1 = p1
        self.player2 = p2
        self.moves = []
    
    def initialize(self):
        pass

    def undo(self):
        pass

class TicTacToe:
    def __init__(self,n) -> None:
        self.board = [[] * n] * n
    
    def move(self, player,row,col):
        m, n = len(self.board), len(self.board[0])
        if (row < 0 or col < 0 or row >= m or col >= n):
            print ("Invalid Move")
        elif (self.board[row][col] != 0):
            print ("cell is already occupied")
        elif (player != 0 and player != 1):
            print ("invalid player")
        else:
            if player == 0:
                player -= 1
            else:
                player += 1
            self.board[row][col] = player
            winRow, winCol, winDiag, winRevDiag = True, True, True, True
            for i in range(m):
                if self.board[row][i] != player:
                    winRow = False
                if self.board[i][col] != player:
                    winCol = False
                if self.board[i][i] != player:
                    winDiag = False
                if self.board[i][n-i-1] != player:
                    winRevDiag = False
            if winRow or winCol or winDiag or winRevDiag :
                return player
            return 0
        
class TicTacToe:
    '''
    we have a TicTacToe class that represents the game. It has a 3x3 board to keep track of the game 
    state and a current_player variable to store the current player (X or O).
    The print_board method prints the current state of the board. The make_move method allows a player 
    to make a move by specifying the row and column. It checks if the move is valid and updates the 
    board accordingly.
    The check_winner method checks if there is a winner by examining the rows, columns, and diagonals. 
    It returns the winning player ('X' or 'O') if there is a winner, or None if there is no winner.
    The is_board_full method checks if the board is full, indicating a tie.
    In the usage example, the game starts, and players take turns making moves until there is a winner 
    or a tie. The board is printed after each move, and the game checks for a winner or a tie condition. 
    The game loop continues until there is a winner or a tie.
    '''
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-----")

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Please try again.")

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        # No winner
        return None

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

# Usage example
if __name__ == "__main__":
    game = TicTacToe()

    while True:
        game.print_board()
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        game.make_move(row, col)

        winner = game.check_winner()
        if winner:
            print(f"Player {winner} wins!")
            break

        if game.is_board_full():
            print("It's a tie!")
            break
