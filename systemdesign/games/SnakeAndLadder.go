package main

import (
	"fmt"
	"math/rand"
	"time"
)

const (
	boardSize    = 100
	numSnakes    = 5
	numLadders   = 5
	snakePenalty = 5
	ladderBonus  = 10
)

var (
	snakes  = map[int]int{}
	ladders = map[int]int{}
)

func init() {
	rand.Seed(time.Now().UnixNano())
	generateSnakesAndLadders()
}

func generateSnakesAndLadders() {
	for i := 0; i < numSnakes; i++ {
		head := rand.Intn(boardSize-10) + 10
		tail := rand.Intn(head-1) + 1
		snakes[head] = tail
	}
	for i := 0; i < numLadders; i++ {
		bottom := rand.Intn(boardSize-10) + 1
		top := rand.Intn(boardSize-bottom) + bottom + 1
		ladders[bottom] = top
	}
}

func rollDice() int {
	return rand.Intn(6) + 1
}

func main() {
	var playerPosition int
	var currentPlayer int

	fmt.Println("Welcome to Snake and Ladder!")

	for playerPosition < boardSize {
		currentPlayer = (currentPlayer + 1) % 2

		fmt.Printf("Player %d's turn (Press Enter to roll the dice)\n", currentPlayer+1)
		fmt.Scanln()

		diceRoll := rollDice()
		fmt.Printf("Player %d rolled a %d\n", currentPlayer+1, diceRoll)

		playerPosition += diceRoll
		if newPosition, ok := snakes[playerPosition]; ok {
			fmt.Printf("Player %d encountered a snake! Moving to position %d\n", currentPlayer+1, newPosition)
			playerPosition = newPosition
		} else if newPosition, ok := ladders[playerPosition]; ok {
			fmt.Printf("Player %d found a ladder! Moving to position %d\n", currentPlayer+1, newPosition)
			playerPosition = newPosition
		}

		if playerPosition > boardSize {
			playerPosition = boardSize - (playerPosition - boardSize)
		}

		fmt.Printf("Player %d is now at position %d\n", currentPlayer+1, playerPosition)

		if playerPosition == boardSize {
			fmt.Printf("Player %d wins!\n", currentPlayer+1)
			break
		}
	}
}
