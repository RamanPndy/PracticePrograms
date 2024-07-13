from systemdesign.games.poker.interface import IPlayerObserver

class Player(IPlayerObserver):
    def __init__(self, name: str):
        self._name = name

    def update(self, game):
        game_info = game.get_game_info()
        print(f"Notification for {self._name}: Game {game_info['game_id']} status is {game_info['status']}")

    def get_name(self):
        return self._name
