package main

import "fmt"

// Set is a custom data structure that uses a map to store unique elements.
type Set struct {
    elements map[interface{}]struct{}
}

// NewSet creates and returns a new Set.
func NewSet() *Set {
    return &Set{
        elements: make(map[interface{}]struct{}),
    }
}

// Add adds an element to the set.
func (s *Set) Add(value interface{}) {
    s.elements[value] = struct{}{}
}

// Remove removes an element from the set.
func (s *Set) Remove(value interface{}) {
    delete(s.elements, value)
}

// Contains checks if an element is in the set.
func (s *Set) Contains(value interface{}) bool {
    _, exists := s.elements[value]
    return exists
}

// Size returns the number of elements in the set.
func (s *Set) Size() int {
    return len(s.elements)
}

// Clear removes all elements from the set.
func (s *Set) Clear() {
    s.elements = make(map[interface{}]struct{})
}

// Values returns all elements in the set as a slice.
func (s *Set) Values() []interface{} {
    keys := make([]interface{}, 0, len(s.elements))
    for key := range s.elements {
        keys = append(keys, key)
    }
    return keys
}

func main() {
    // Create a new set
    set := NewSet()

    // Add elements to the set
    set.Add(1)
    set.Add(2)
    set.Add(3)

    // Check if elements are in the set
    fmt.Println("Contains 2:", set.Contains(2)) // Output: Contains 2: true
    fmt.Println("Contains 4:", set.Contains(4)) // Output: Contains 4: false

    // Remove an element from the set
    set.Remove(2)

    // Check the size of the set
    fmt.Println("Size:", set.Size()) // Output: Size: 2

    // Get all elements in the set
    fmt.Println("Elements:", set.Values()) // Output: Elements: [1 3]

    // Clear the set
    set.Clear()

    // Check the size of the set after clearing
    fmt.Println("Size after clearing:", set.Size()) // Output: Size after clearing: 0
}
