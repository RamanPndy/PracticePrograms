# Create a new game
from systemdesign.games.chess.game import Game

game = Game()

# Display the initial board
game.display_board()

# Make a move (white pawn moves forward)
game.move((6, 4), (4, 4))

# Display the board after the move
game.display_board()
