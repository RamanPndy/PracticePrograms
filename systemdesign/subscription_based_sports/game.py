from typing import List
from datetime import datetime

from systemdesign.subscription_based_sports.interface import IGameSubject

class Game(IGameSubject):
    def __init__(self, game_id: int, teams: List[str], sport: str):
        self._game_id = game_id
        self._teams = teams
        self._sport = sport
        self._score = [0, 0]  # Initial score for each team
        self._status = "Scheduled"  # Possible statuses: Scheduled, In Progress, Finished
        self._start_time = None
        self._subscribers = []

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self)

    def update_score(self, team_index: int, score: int):
        self._score[team_index] += score
        self.notify()

    def update_status(self, new_status: str):
        self._status = new_status
        self.notify()

    def start_game(self):
        self._status = "In Progress"
        self._start_time = datetime.now()
        self.notify()

    def end_game(self):
        self._status = "Finished"
        self.notify()

    def get_game_info(self):
        return {
            'game_id': self._game_id,
            'teams': self._teams,
            'sport': self._sport,
            'score': self._score,
            'status': self._status,
            'start_time': self._start_time
        }
