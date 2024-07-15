from systemdesign.games.poker.client import PokerGameSystem
from systemdesign.games.poker.player import Player

poker_system = PokerGameSystem()

poker_system.create_game(1)

player1 = Player("Alice")
player2 = Player("Bob")

poker_system.add_player_to_game(1, player1)
poker_system.add_player_to_game(1, player2)

poker_system.update_game_status(1, "In Progress")
poker_system.update_game_score(1, player1, 100)
poker_system.update_game_score(1, player2, 200)

poker_system.update_game_status(1, "Finished")
