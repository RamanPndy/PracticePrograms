package golang

import (
	"fmt"
	"time"
)

// Channels are the pipes that connect concurrent goroutines.

// In buffered channel, we can send values into the channel without a corresponding concurrent receive.

func main() {
	// Here we `make` a channel of strings buffering up to 2 values.
	messages := make(chan string, 2)

	// Because this channel is buffered, we can send these values into the channel without a corresponding
	// concurrent receive.
	messages <- "buffered"
	messages <- "channel"

	// Later we can receive these two values as usual.
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}

// Channel Synchronization
// We can use channels to synchronize execution across goroutines.

func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	done <- true
}

func main() {
	done := make(chan bool, 1)
	go worker(done)

	<-done // If we removed the <- done line from this program, the program would exit before the worker even started.
}

// Channel Directions
func ping(pings chan<- string, msg string) {
	pings <- msg
}

func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}

// By default channels are unbuffered, meaning that they will only accept sends (chan <-) if there is a corresponding 
// receive (<- chan) ready to receive the sent value.
// Buffered channels accept a limited number of values without a corresponding receiver for those values.

func main() {

	messages := make(chan string, 2)

	messages <- "buffered"
	messages <- "channel"

	fmt.Println(<-messages)
	fmt.Println(<-messages)
}

Unbuffered Channels:
An unbuffered channel has a capacity of zero. 
This means that every send operation on the channel must be matched by a corresponding receive operation, 
creating a synchronization point between the sender and receiver.
When a value is sent on an unbuffered channel, the sender blocks until another goroutine receives the value.
Unbuffered channels are often used when you need to ensure that a communication between goroutines is synchronized, 
meaning the sender and receiver must be ready to communicate at the same time.

Example:
ch := make(chan int) // unbuffered channel
go func() {
    value := 42
    ch <- value // sending value to the channel
}()
result := <-ch // receiving value from the channel

Buffered Channels:
A buffered channel has a specified capacity greater than zero. 
This means that it can hold a certain number of elements without a corresponding receiver being ready.
When a value is sent on a buffered channel, the sender can continue execution unless the channel is full. 
Similarly, when receiving from a buffered channel, the receiver can continue unless the channel is empty.
Buffered channels are useful when you want to decouple the sender and receiver, 
allowing them to operate independently as long as the buffer doesnt overflow or underflow.

Example:
ch := make(chan int, 3) // buffered channel with capacity 3
go func() {
    ch <- 1 // sending value to the buffered channel
    ch <- 2
}()
value1 := <-ch // receiving value from the channel
value2 := <-ch

Channel Synchronization
Blocking Operations with Channels:
Channels in Go can be used to perform blocking operations. 
When a goroutine attempts to send or receive data on a channel, it blocks until another goroutine is ready to receive or send, 
respectively. This blocking behavior helps in synchronizing the execution flow.

// Creating a channel
ch := make(chan int)

// Goroutine sending data to the channel
go func() {
    ch <- 42 // Sends data to channel
}()

// Receiving data from the channel (blocking operation)
value := <-ch // Receives data from channel
fmt.Println(value) // Prints 42


Synchronization Patterns:
Wait Group: The sync.WaitGroup type is commonly used for synchronizing goroutines. 
It allows one goroutine to wait for a group of goroutines to finish their execution before proceeding.

var wg sync.WaitGroup

// Increment the WaitGroup counter
wg.Add(1)

// Start a goroutine
go func() {
    defer wg.Done() // Decrement the WaitGroup counter when done
    // Perform some task
}()

// Wait for all goroutines to finish
wg.Wait()

Done Channel: You can also use a done channel to signal the completion of a goroutine. 
This is especially useful when you have multiple goroutines and want to know when all of them have finished.
done := make(chan struct{})

// Start a goroutine
go func() {
    defer close(done) // Signal completion by closing the done channel
    // Perform some task
}()

// Wait for the goroutine to finish
<-done

Select Statement for Channel Synchronization:
The select statement in Go is used with channels to wait for multiple channel operations simultaneously. 
This is often used for coordinating multiple goroutines or handling timeouts.

ch1 := make(chan int)
ch2 := make(chan int)

// Start goroutine to send data on ch1
go func() {
    ch1 <- 42
}()

// Start goroutine to send data on ch2
go func() {
    ch2 <- 100
}()

// Select statement for synchronization
select {
case value := <-ch1:
    fmt.Println("Received from ch1:", value)
case value := <-ch2:
    fmt.Println("Received from ch2:", value)
}

Buffered Channels for Non-Blocking Synchronization:
Buffered channels can also be used for synchronization, especially in cases where non-blocking behavior is desired. 
However, care should be taken to avoid potential deadlocks.

// Buffered channel with capacity 1
ch := make(chan int, 1)

// Send data to the channel (non-blocking)
select {
case ch <- 42:
    fmt.Println("Sent data to channel")
default:
    fmt.Println("Channel buffer is full")
}

// Receive data from the channel (non-blocking)
select {
case value := <-ch:
    fmt.Println("Received from channel:", value)
default:
    fmt.Println("Channel is empty")
}

