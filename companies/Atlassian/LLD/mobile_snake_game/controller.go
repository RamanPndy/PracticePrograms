package mobilesnakegame

import "time"

//Uses Strategy Pattern for movement logic and Observer Pattern for rendering updates.

type GameEngine struct {
	State            *GameState
	Board            Board
	Renderer         IRenderer
	InputHandler     IInputHandler
	CollisionService ICollisionService
	FoodService      IFoodService
	TickRate         time.Duration
}

func (g *GameEngine) Start() {
	ticker := time.NewTicker(g.TickRate)

	for range ticker.C {
		if g.State.Over || !g.State.Running {
			return
		}

		g.step()
		g.Renderer.Render(g.State)
	}
}

func (g *GameEngine) step() {
	dir := g.InputHandler.GetDirection()
	g.moveSnake(dir)

	if g.CollisionService.IsWallCollision(*g.State.Snake, g.Board) ||
		g.CollisionService.IsSelfCollision(*g.State.Snake) {
		g.State.Over = true
		g.Renderer.RenderGameOver(g.State)
		return
	}

	g.checkFoodAndGrow()
}

func (g *GameEngine) moveSnake(dir Direction) {
	snake := g.State.Snake
	head := snake.Body[0]

	next := head
	switch dir {
	case Up:
		next.Y--
	case Down:
		next.Y++
	case Left:
		next.X--
	case Right:
		next.X++
	}

	newBody := append([]Position{next}, snake.Body[:len(snake.Body)-1]...)
	snake.Body = newBody
}

func (g *GameEngine) checkFoodAndGrow() {
	snake := g.State.Snake
	if snake.Body[0] == g.State.Food.Location {
		g.State.Score += 1

		tail := snake.Body[len(snake.Body)-1]
		snake.Body = append(snake.Body, tail)

		g.State.Food.Location = g.FoodService.SpawnFood(g.Board, *snake)
	}
}
