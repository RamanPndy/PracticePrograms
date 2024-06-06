'''
Step-by-Step Design
Board: Represent the game board which includes snakes and ladders.
Snake: Represents a snake on the board.
Ladder: Represents a ladder on the board.
Player: Represents a player in the game.
Game: Manages the game flow including players' turns and win conditions.
Dice: Represents the dice used in the game.
'''
class Board:
    def __init__(self, size=100):
        self.size = size
        self.snakes = {}
        self.ladders = {}
    
    def add_snake(self, head, tail):
        self.snakes[head] = tail

    def add_ladder(self, start, end):
        self.ladders[start] = end

    def get_position(self, position):
        while position in self.snakes or position in self.ladders:
            if position in self.snakes:
                position = self.snakes[position]
            elif position in self.ladders:
                position = self.ladders[position]
        return position

class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps

    def set_position(self, position):
        self.position = position

import random

class Game:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.dice = Dice()
        self.winner = None

    def play(self):
        while not self.winner:
            for player in self.players:
                steps = self.dice.roll()
                player.move(steps)
                next_position = self.board.get_position(player.position)
                player.set_position(next_position)
                
                if player.position >= self.board.size:
                    self.winner = player
                    break

        print(f"{self.winner.name} wins the game!")

class Dice:
    def roll(self):
        return random.randint(1, 6)
