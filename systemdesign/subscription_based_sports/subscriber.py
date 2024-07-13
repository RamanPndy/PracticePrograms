from systemdesign.subscription_based_sports.interface import ISubscriber

class Subscriber(ISubscriber):
    def __init__(self, username: str):
        self._username = username

    def update(self, game):
        game_info = game.get_game_info()
        print(f"Notification for {self._username}: Game {game_info['game_id']} updated - {game_info['status']}")
