package main

import (
	"fmt"
)

// Node represents a node in the linked list
type Node struct {
	data int
	next *Node
}

// LinkedList represents the linked list
type LinkedList struct {
	head *Node
}

// Insert adds a new node at the end of the list
func (ll *LinkedList) Insert(value int) {
	newNode := &Node{data: value}
	if ll.head == nil {
		ll.head = newNode
	} else {
		current := ll.head
		for current.next != nil {
			current = current.next
		}
		current.next = newNode
	}
}

// Delete removes the first occurrence of a node with the given value
func (ll *LinkedList) Delete(value int) {
	if ll.head == nil {
		fmt.Println("List is empty")
		return
	}

	// If the node to be deleted is the head node
	if ll.head.data == value {
		ll.head = ll.head.next
		return
	}

	// Find the node to be deleted
	current := ll.head
	for current.next != nil && current.next.data != value {
		current = current.next
	}

	// If the node was found, remove it
	if current.next != nil {
		current.next = current.next.next
	} else {
		fmt.Println("Value not found in the list")
	}
}

// Display prints all the nodes in the list
func (ll *LinkedList) Display() {
	if ll.head == nil {
		fmt.Println("List is empty")
		return
	}

	current := ll.head
	for current != nil {
		fmt.Printf("%d -> ", current.data)
		current = current.next
	}
	fmt.Println("nil")
}

func main() {
	ll := LinkedList{}

	ll.Insert(10)
	ll.Insert(20)
	ll.Insert(30)
	ll.Display() // Output: 10 -> 20 -> 30 -> nil

	ll.Delete(20)
	ll.Display() // Output: 10 -> 30 -> nil

	ll.Delete(40) // Output: Value not found in the list
}
