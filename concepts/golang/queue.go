package main

import "fmt"

// Queue represents a basic queue data structure.
type Queue struct {
	items []interface{}
}

// Enqueue adds an item to the end of the queue.
func (q *Queue) Enqueue(item interface{}) {
	q.items = append(q.items, item)
}

// Dequeue removes and returns the front item from the queue.
func (q *Queue) Dequeue() interface{} {
	if len(q.items) == 0 {
		return nil
	}
	frontItem := q.items[0]
	q.items = q.items[1:]
	return frontItem
}

// Front returns the front item from the queue without removing it.
func (q *Queue) Front() interface{} {
	if len(q.items) == 0 {
		return nil
	}
	return q.items[0]
}

// IsEmpty returns true if the queue is empty.
func (q *Queue) IsEmpty() bool {
	return len(q.items) == 0
}

// Size returns the number of items in the queue.
func (q *Queue) Size() int {
	return len(q.items)
}

func main() {
	queue := Queue{}

	queue.Enqueue(10)
	queue.Enqueue(20)
	queue.Enqueue(30)

	fmt.Println("Size:", queue.Size())
	fmt.Println("Front:", queue.Front())

	fmt.Println("Dequeue:", queue.Dequeue())
	fmt.Println("Size:", queue.Size())

	fmt.Println("Dequeue:", queue.Dequeue())
	fmt.Println("IsEmpty:", queue.IsEmpty())

	fmt.Println("Dequeue:", queue.Dequeue())
	fmt.Println("IsEmpty:", queue.IsEmpty())
}
