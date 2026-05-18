package mobilesnakegame

type Position struct {
	X int
	Y int
}

type Direction int

const (
	Up Direction = iota
	Down
	Left
	Right
)

type Snake struct {
	Body      []Position
	Direction Direction
}

type Food struct {
	Location Position
}

type Board struct {
	Width  int
	Height int
}

type GameState struct {
	Snake   *Snake
	Food    *Food
	Score   int
	Running bool
	Over    bool
}
