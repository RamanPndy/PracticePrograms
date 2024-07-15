+-----------------------------+        +-----------------------------+
|        IGameSubject         |        |        IPlayerObserver      |
+-----------------------------+        +-----------------------------+
| + attach(observer)          |        | + update(game)              |
| + detach(observer)          |        +-----------------------------+
| + notify()                  |
+-----------------------------+
          ^                                   ^
          |                                   |
+-----------------------------+        +-----------------------------+
|            Game             |        |           Player            |
+-----------------------------+        +-----------------------------+
| - _game_id: int             |        | - _name: str                |
| - _players: List[Player]    |        | + update(game)              |
| - _scores: Dict[Player, int]|        | + get_name() -> str         |
| - _status: str              |        +-----------------------------+
| - _history: List[str]       |
| - _observers: List[IPlayerObserver]  |
| + attach(observer)          |
| + detach(observer)          |
| + notify()                  |
| + add_player(player)        |
| + remove_player(player)     |
| + update_score(player, score)|
| + update_status(new_status) |
| + get_game_info() -> dict   |
+-----------------------------+

+-----------------------------+
|         GameHistory         |
+-----------------------------+
| - _history: List[str]       |
| + add_event(event)          |
| + get_history() -> List[str]|
+-----------------------------+

+-----------------------------+
|       PokerGameSystem       |
+-----------------------------+
| - _games: Dict[int, Game]   |
| + create_game(game_id)      |
| + get_game(game_id) -> Game |
| + add_player_to_game(game_id, player)|
| + remove_player_from_game(game_id, player)|
| + update_game_score(game_id, player, score)|
| + update_game_status(game_id, status)|
+-----------------------------+
