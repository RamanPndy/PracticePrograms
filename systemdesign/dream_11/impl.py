from typing import Dict, List
from systemdesign.dream_11.interface import IContestService, IMatchService, IScoreService, ITeamService

class MatchService(IMatchService):
    def __init__(self):
        self.matches = []

    def view_ongoing_matches(self) -> List[Dict]:
        return self.matches

    def add_match(self, match_id: str, teams: List[str]):
        self.matches.append({"match_id": match_id, "teams": teams})

class TeamService(ITeamService):
    def __init__(self):
        self.teams = {}

    def create_fantasy_team(self, user_id: str, team_name: str, players: List[str]):
        self.teams[user_id] = {"team_name": team_name, "players": players}

class ContestService(IContestService):
    def __init__(self):
        self.contests = {}
        self.user_contests = {}

    def create_contest(self, contest_name: str, entry_fee: float, prize_pool: float):
        contest_id = len(self.contests) + 1
        self.contests[contest_id] = {"contest_name": contest_name, "entry_fee": entry_fee, "prize_pool": prize_pool}
        return contest_id

    def join_contest(self, user_id: str, contest_id: str):
        if contest_id in self.contests:
            if user_id in self.user_contests:
                self.user_contests[user_id].append(contest_id)
            else:
                self.user_contests[user_id] = [contest_id]

class ScoreService(IScoreService):
    def __init__(self):
        self.scores = {}
        self.subscribers = []

    def calculate_scores(self):
        # Real-time score calculation logic
        for subscriber in self.subscribers:
            subscriber.update_score()

    def get_user_score(self, user_id: str) -> int:
        return self.scores.get(user_id, 0)

    def subscribe(self, user):
        self.subscribers.append(user)

    def unsubscribe(self, user):
        self.subscribers.remove(user)

class User:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.score = 0

    def update_score(self):
        # Update score logic
        pass
