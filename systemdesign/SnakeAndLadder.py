import random

class Player:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

class Dice:
    def rollDice(self):
        return random.randint(1,10)

class Jumper:
    def __init__(self, startPoint, endPoint) -> None:
        self.startPoint = startPoint
        self.endPoint = endPoint
    
    def isLadder(self):
        return self.startPoint < self.endPoint
    
    def isSnake(self):
        return self.startPoint > self.endPoint

class GameBoard:
    def __init__(self, boardSize) -> None:
        self.boardSize = boardSize
        self.dice = Dice()
        self.nextTurn = list()
        self.snakes = list()
        self.ladders = list()
        self.playersCurrentPosition = dict()
    
    def play(self):
        while len(self.nextTurn) > 1:
            player = self.nextTurn.pop(0)
            currentPosition = self.playersCurrentPosition(player.name)
            diceValue = self.dice.rollDice()
            nextCell = currentPosition + diceValue
            if nextCell > self.boardSize:
                self.nextTurn.append(player)
            elif nextCell == self.boardSize:
                print (player.name + "has won the game")
            else:
                nextPosition = nextCell
                for snake in self.snakes:
                    if snake.startPoint == nextPosition:
                        nextPosition = snake.endPoint
                if nextPosition != nextCell:
                    print (player.name + "Bitten by Snake at position : " + nextCell)
                playerGotLadder = False
                for ladder in self.ladders:
                    if ladder.startPoint == nextPosition:
                        nextPosition = ladder.endPoint
                        playerGotLadder = True
                if nextPosition != nextCell and playerGotLadder:
                    print (player.name + "Got Ladder at position : " + nextCell)
                if nextPosition == self.boardSize:
                    print (player.name + "has won the game")
                else:
                    self.playersCurrentPosition[player.name, nextPosition]
                    print (player.name + "is at position : " + nextPosition)
                    self.nextTurn.append(player)
                