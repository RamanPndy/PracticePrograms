package main

import "fmt"

/*
Generics allow our functions or data structures to take in several types that are defined in their generic form.
*/

type GenericSlice[T any] []T

type Stack[T any] struct {
	data []T
}

func (s *Stack[T]) Push(v T) {
	s.data = append(s.data, v)
}

func (s *Stack[T]) Pop() (T, bool) {
	if len(s.data) == 0 {
		var zero T
		return zero, false
	}
	lastIndex := len(s.data) - 1
	value := s.data[lastIndex]
	s.data = s.data[:lastIndex]
	return value, true
}

func (s *Stack[T]) Size() int {
	return len(s.data)
}

func Print[T any](s []T) {
	for _, v := range s {
		fmt.Print(v)
	}
}

func Equal[T comparable](a, b T) bool {
	return a == b
}

func (g GenericSlice[T]) Print() {
	for _, v := range g {
		fmt.Println(v)
	}
}

func PrintGeneric[T any](g GenericSlice[T]) {
	for _, v := range g {
		fmt.Println(v)
	}
}

func main() {
	Print([]string{"Hello, ", "playground\n"})
	Print([]int{1, 2, 3})
	Equal("a", "a")

	g := GenericSlice[int]{1, 2, 3}
	g.Print()       //1 2 3
	PrintGeneric(g) //1 2 3

	intStack := Stack[int]{}
	intStack.Push(1)
	intStack.Push(2)
	intStack.Push(3)

	fmt.Println(intStack.Pop())  // Output: 3, true
	fmt.Println(intStack.Size()) // Output: 2

	stringStack := Stack[string]{}
	stringStack.Push("hello")
	stringStack.Push("world")

	fmt.Println(stringStack.Pop())  // Output: world, true
	fmt.Println(stringStack.Size()) // Output: 1
}
