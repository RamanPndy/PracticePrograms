+---------------------+         +-----------------------+
|      GameEngine     |-------> |     IRenderer         |
+---------------------+         +-----------------------+
| - State: GameState  |         | + Render()            |
| - Board: Board      |         | + RenderGameOver()    |
| - InputHandler      |
| - FoodService       |
| - CollisionService  |
| - TickRate          |
+---------+-----------+
          |
          | uses
          |
+---------v----------+          +-----------------------+
|     Snake          |          |     IFoodService      |
+--------------------+          +-----------------------+
| Body: []Position   |          | + SpawnFood()         |
| Direction          |          +-----------------------+

+--------------------+          +-----------------------+
|   ICollisionSvc    |          |      GameState        |
+--------------------+          +-----------------------+
|+IsWallCollision    |          | Snake, Food, Score    |
|+IsSelfCollision    |          | Running, Over         |
+--------------------+          +-----------------------+
