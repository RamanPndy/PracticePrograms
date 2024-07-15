from typing import List
from systemdesign.subscription_based_sports.game import Game
from systemdesign.subscription_based_sports.interface import ISubscriber

class SportsWebsite:
    def __init__(self):
        self._games = {}

    def add_game(self, game_id: int, teams: List[str], sport: str):
        if game_id not in self._games:
            game = Game(game_id, teams, sport)
            self._games[game_id] = game
        else:
            print(f"Game with ID {game_id} already exists.")

    def get_game(self, game_id: int):
        return self._games.get(game_id)

    def subscribe_to_game(self, game_id: int, subscriber: ISubscriber):
        game = self.get_game(game_id)
        if game:
            game.attach(subscriber)
        else:
            print(f"Game with ID {game_id} not found.")

    def unsubscribe_from_game(self, game_id: int, subscriber: ISubscriber):
        game = self.get_game(game_id)
        if game:
            game.detach(subscriber)
        else:
            print(f"Game with ID {game_id} not found.")

    def simulate_game_progress(self, game_id: int):
        game = self.get_game(game_id)
        if game:
            game.start_game()
            game.update_score(0, 3)
            game.update_score(1, 2)
            game.end_game()
        else:
            print(f"Game with ID {game_id} not found.")
