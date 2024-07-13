from systemdesign.subscription_based_sports.client import SportsWebsite
from systemdesign.subscription_based_sports.subscriber import Subscriber

website = SportsWebsite()

website.add_game(1, ["Team A", "Team B"], "Football")
website.add_game(2, ["Team X", "Team Y"], "Basketball")

subscriber1 = Subscriber("User1")
subscriber2 = Subscriber("User2")

website.subscribe_to_game(1, subscriber1)
website.subscribe_to_game(1, subscriber2)

website.simulate_game_progress(1)

website.unsubscribe_from_game(1, subscriber2)

website.simulate_game_progress(1)