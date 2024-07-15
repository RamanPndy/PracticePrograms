Use Cases

Create Game:
Description: A new poker game is created with a unique game ID.
Actors: System Admin
Preconditions: The game ID must not already exist.
Postconditions: The game is added to the system.

Add Player to Game:
Description: A player joins an existing poker game.
Actors: Player
Preconditions: The game must exist, and the player must not already be in the game.
Postconditions: The player is added to the game's player list and starts receiving updates.

Update Game Score:
Description: The score of a player in a poker game is updated.
Actors: Game System
Preconditions: The player must be part of the game.
Postconditions: The player's score is updated, and all observers (players) are notified.

Update Game Status:
Description: The status of a poker game is updated.
Actors: Game System
Preconditions: The game must exist.
Postconditions: The game's status is updated, and all observers (players) are notified.
