package main

/*
An empty struct in Go, also known as a zero-byte struct, is a struct type with no fields defined. It is declared as struct{}.
While it may seem unusual to define a struct with no fields, empty structs have several use cases in Go:

Signaling and Synchronization:
Empty structs are commonly used for signaling and synchronization purposes, especially in concurrent programming with channels.
Since an empty struct consumes no memory (it has zero size), it's lightweight and efficient for signaling events or
synchronization points without carrying any data.

Channel Signaling:
Empty structs can be used as values in channels to signal events or indicate completion.
For example, you might have a channel doneCh chan struct{} that is used to signal when a goroutine has completed its task.

Map Keys:
Empty structs can be used as keys in maps when you want a set-like data structure with no associated values.
Using an empty struct as a map key creates a memory-efficient set implementation in Go.

Type Assertions and Interfaces:
Empty structs can be used in type assertions or as placeholders in interfaces.
For instance, if you have an interface MyInterface with no methods, you can use an empty struct as its implementation
placeholder: type MyImplementation struct{}; func (m MyImplementation) Method() {}.

Memory Optimization:
In some cases, empty structs can be used to save memory when you need to represent a concept without any additional data.
For example, if you only need to track the existence of certain items without any associated data, using an empty struct can
avoid allocating memory for unnecessary fields.
Here's an example demonstrating the use of empty structs for signaling and synchronization with channels:*/

import (
	"fmt"
	"time"
)

func worker(doneCh chan struct{}) {
	fmt.Println("Worker: Starting work...")
	time.Sleep(time.Second)
	fmt.Println("Worker: Work completed.")
	doneCh <- struct{}{} // Signal completion by sending an empty struct
}

func main() {
	doneCh := make(chan struct{})

	go worker(doneCh)

	// Block until the worker signals completion
	<-doneCh
	fmt.Println("Main: Worker signaled completion.")
}
