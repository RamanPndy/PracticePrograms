from systemdesign.games.poker.interface import IGameSubject

class Game(IGameSubject):
    def __init__(self, game_id: int):
        self._game_id = game_id
        self._players = []
        self._scores = {}
        self._status = "Waiting"  # Possible statuses: Waiting, In Progress, Finished
        self._history = []
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def add_player(self, player):
        self._players.append(player)
        self._scores[player] = 0
        self.attach(player)

    def remove_player(self, player):
        self._players.remove(player)
        del self._scores[player]
        self.detach(player)

    def update_score(self, player, score):
        if player in self._scores:
            self._scores[player] = score
            self._history.append(f"{player.get_name()} score updated to {score}")
            self.notify()

    def update_status(self, new_status: str):
        self._status = new_status
        self._history.append(f"Game status updated to {new_status}")
        self.notify()

    def get_game_info(self):
        return {
            'game_id': self._game_id,
            'players': [player.get_name() for player in self._players],
            'scores': self._scores,
            'status': self._status,
            'history': self._history
        }

class GameHistory:
    def __init__(self):
        self._history = []

    def add_event(self, event: str):
        self._history.append(event)

    def get_history(self):
        return self._history
