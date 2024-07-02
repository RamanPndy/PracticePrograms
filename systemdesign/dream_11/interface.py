from abc import ABC, abstractmethod
from typing import List, Dict

class IMatchService(ABC):
    @abstractmethod
    def view_ongoing_matches(self) -> List[Dict]:
        pass

class ITeamService(ABC):
    @abstractmethod
    def create_fantasy_team(self, user_id: str, team_name: str, players: List[str]):
        pass

class IContestService(ABC):
    @abstractmethod
    def create_contest(self, contest_name: str, entry_fee: float, prize_pool: float):
        pass

    @abstractmethod
    def join_contest(self, user_id: str, contest_id: str):
        pass

class IScoreService(ABC):
    @abstractmethod
    def calculate_scores(self):
        pass

    @abstractmethod
    def get_user_score(self, user_id: str) -> int:
        pass
