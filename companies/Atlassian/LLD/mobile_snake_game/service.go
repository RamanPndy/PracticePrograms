package mobilesnakegame

import "math/rand"

type FoodService struct{}

func (f *FoodService) SpawnFood(board Board, snake Snake) Position {
	for {
		pos := Position{rand.Intn(board.Width), rand.Intn(board.Height)}
		occupied := false
		for _, s := range snake.Body {
			if s == pos {
				occupied = true
				break
			}
		}
		if !occupied {
			return pos
		}
	}
}

type CollisionService struct{}

func (c *CollisionService) IsWallCollision(snake Snake, board Board) bool {
	head := snake.Body[0]
	return head.X < 0 || head.X >= board.Width || head.Y < 0 || head.Y >= board.Height
}

func (c *CollisionService) IsSelfCollision(snake Snake) bool {
	head := snake.Body[0]
	for _, b := range snake.Body[1:] {
		if b == head {
			return true
		}
	}
	return false
}
