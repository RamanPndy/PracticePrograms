from systemdesign.games.poker.game import Game
from systemdesign.games.poker.player import Player

class PokerGameSystem:
    def __init__(self):
        self._games = {}

    def create_game(self, game_id: int):
        if game_id not in self._games:
            game = Game(game_id)
            self._games[game_id] = game
        else:
            print(f"Game with ID {game_id} already exists.")

    def get_game(self, game_id: int):
        return self._games.get(game_id)

    def add_player_to_game(self, game_id: int, player: Player):
        game = self.get_game(game_id)
        if game:
            game.add_player(player)
        else:
            print(f"Game with ID {game_id} not found.")

    def remove_player_from_game(self, game_id: int, player: Player):
        game = self.get_game(game_id)
        if game:
            game.remove_player(player)
        else:
            print(f"Game with ID {game_id} not found.")

    def update_game_score(self, game_id: int, player: Player, score: int):
        game = self.get_game(game_id)
        if game:
            game.update_score(player, score)
        else:
            print(f"Game with ID {game_id} not found.")

    def update_game_status(self, game_id: int, status: str):
        game = self.get_game(game_id)
        if game:
            game.update_status(status)
        else:
            print(f"Game with ID {game_id} not found.")