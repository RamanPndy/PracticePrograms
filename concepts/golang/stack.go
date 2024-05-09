package main

import (
	"fmt"
)

// Stack represents a stack data structure.
type Stack struct {
	items []interface{}
}

// Push adds an item to the top of the stack.
func (s *Stack) Push(item interface{}) {
	s.items = append(s.items, item)
}

// Pop removes and returns the top item from the stack.
func (s *Stack) Pop() interface{} {
	if len(s.items) == 0 {
		return nil
	}
	topIndex := len(s.items) - 1
	topItem := s.items[topIndex]
	s.items = s.items[:topIndex]
	return topItem
}

// Peek returns the top item from the stack without removing it.
func (s *Stack) Peek() interface{} {
	if len(s.items) == 0 {
		return nil
	}
	return s.items[len(s.items)-1]
}

// IsEmpty returns true if the stack is empty.
func (s *Stack) IsEmpty() bool {
	return len(s.items) == 0
}

// Size returns the number of items in the stack.
func (s *Stack) Size() int {
	return len(s.items)
}

func main() {
	stack := Stack{}

	stack.Push(10)
	stack.Push(20)
	stack.Push(30)

	fmt.Println("Size:", stack.Size())
	fmt.Println("Peek:", stack.Peek())

	fmt.Println("Pop:", stack.Pop())
	fmt.Println("Size:", stack.Size())

	fmt.Println("Pop:", stack.Pop())
	fmt.Println("IsEmpty:", stack.IsEmpty())

	fmt.Println("Pop:", stack.Pop())
	fmt.Println("IsEmpty:", stack.IsEmpty())
}
