package golang

import (
	"fmt"
	"time"
)

// Channels are the pipes that connect concurrent goroutines.

// In buffered channel, we can send values into the channel without a corresponding concurrent receive.

func main() {
	// Here we `make` a channel of strings buffering up to
	// 2 values.
	messages := make(chan string, 2)

	// Because this channel is buffered, we can send these
	// values into the channel without a corresponding
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

// By default channels are unbuffered, meaning that they will only accept sends (chan <-) if there is a corresponding receive (<- chan) ready to receive the sent value.
// Buffered channels accept a limited number of values without a corresponding receiver for those values.

func main() {

	messages := make(chan string, 2)

	messages <- "buffered"
	messages <- "channel"

	fmt.Println(<-messages)
	fmt.Println(<-messages)
}
