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