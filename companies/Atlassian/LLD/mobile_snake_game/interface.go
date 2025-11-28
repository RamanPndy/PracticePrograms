package mobilesnakegame

type IRenderer interface {
	Render(state *GameState)
	RenderGameOver(state *GameState)
}

type IFoodService interface {
	SpawnFood(board Board, snake Snake) Position
}

type ICollisionService interface {
	IsWallCollision(snake Snake, board Board) bool
	IsSelfCollision(snake Snake) bool
}

type IInputHandler interface {
	GetDirection() Direction
}

type IGameLoop interface {
	Start()
	Stop()
}
