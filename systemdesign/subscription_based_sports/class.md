+-----------------------------+        +-----------------------------+
|        IGameSubject         |        |         ISubscriber         |
+-----------------------------+        +-----------------------------+
| + attach(subscriber)        |        | + update(game)              |
| + detach(subscriber)        |        +-----------------------------+
| + notify()                  |
+-----------------------------+
          ^
          |
+-----------------------------+        +-----------------------------+
|            Game             |------->|         Subscriber          |
+-----------------------------+        +-----------------------------+
| - _game_id: int              |        | - _username: str             |
| - _teams: List[str]          |        +-----------------------------+
| - _sport: str                |
| - _score: List[int]          |
| - _status: str               |
| - _start_time: datetime      |
| - _subscribers: List[ISubscriber] |
| + attach(subscriber)        |
| + detach(subscriber)        |
| + notify()                  |
| + update_score(team_index, score) |
| + update_status(new_status)  |
| + start_game()              |
| + end_game()                |
| + get_game_info() -> dict   |
+-----------------------------+
