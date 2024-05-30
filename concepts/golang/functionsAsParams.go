package main

import (
	"fmt"
)

// Define a function type that accepts an int and returns an int
type IntFunction func(int) int

// Function that accepts a slice of IntFunction and an int
func applyFunctions(funcs []IntFunction, value int) {
	for _, fn := range funcs {
		fmt.Println(fn(value))
	}
}

// Example functions to pass
func addOne(n int) int {
	return n + 1
}

func square(n int) int {
	return n * n
}

func main() {
	// Create a slice of functions
	funcs := []IntFunction{addOne, square}

	// Call applyFunctions with the slice of functions and a value
	applyFunctions(funcs, 5)
}
