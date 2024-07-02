# Create services
from systemdesign.dream_11.factory import ServiceFactory


match_service = ServiceFactory.get_match_service()
team_service = ServiceFactory.get_team_service()
contest_service = ServiceFactory.get_contest_service()
score_service = ServiceFactory.get_score_service()

# Add a match
match_service.add_match("match1", ["Team A", "Team B"])

# View ongoing matches
print(match_service.view_ongoing_matches())

# Create a fantasy team
team_service.create_fantasy_team("user1", "Dream Team", ["player1", "player2", "player3"])

# Create and join a contest
contest_id = contest_service.create_contest("Super Contest", 10.0, 100.0)
contest_service.join_contest("user1", contest_id)

# Calculate and get user score
score_service.calculate_scores()
print(score_service.get_user_score("user1"))
