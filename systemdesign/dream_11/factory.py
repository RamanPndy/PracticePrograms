from systemdesign.dream_11.impl import ContestService, MatchService, ScoreService, TeamService
from systemdesign.dream_11.interface import IContestService, IMatchService, IScoreService, ITeamService

class ServiceFactory:
    @staticmethod
    def get_match_service() -> IMatchService:
        return MatchService()

    @staticmethod
    def get_team_service() -> ITeamService:
        return TeamService()

    @staticmethod
    def get_contest_service() -> IContestService:
        return ContestService()

    @staticmethod
    def get_score_service() -> IScoreService:
        return ScoreService()
