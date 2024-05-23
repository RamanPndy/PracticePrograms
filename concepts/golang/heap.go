package main

import (
	"container/heap"
	"fmt"
)

// An IntHeap is a min-heap of integers.
type IntHeap []int

// Len returns the number of elements in the heap.
func (h IntHeap) Len() int { return len(h) }

// Less returns true if element at index i should sort before the element at index j.
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }

// Swap swaps the elements at indices i and j.
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

// Push pushes an element onto the heap.
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

// Pop removes and returns the smallest element from the heap.
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func main() {
	// Create a new IntHeap and initialize it as a heap.
	h := &IntHeap{2, 1, 5}
	heap.Init(h)

	// Push some new elements onto the heap.
	heap.Push(h, 3)
	heap.Push(h, 7)

	// Print the minimum element.
	fmt.Printf("min: %d\n", (*h)[0])

	// Pop the minimum element and print it.
	fmt.Printf("pop: %d\n", heap.Pop(h))

	// Print the remaining elements in the heap.
	for h.Len() > 0 {
		fmt.Printf("%d ", heap.Pop(h))
	}
}
