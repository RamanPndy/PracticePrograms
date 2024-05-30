package main

import (
	"context"
	"fmt"
	"time"
)

func worker(ctx context.Context, id int) {
	for {
		select {
		case <-ctx.Done():
			fmt.Printf("Worker %d: received cancellation signal\n", id)
			return
		default:
			fmt.Printf("Worker %d: working...\n", id)
			time.Sleep(500 * time.Millisecond)
		}
	}
}

func main() {
	// Create a background context
	mainCtx := context.Background()

	// First goroutine with the background context (it will run indefinitely)
	go worker(mainCtx, 1)

	// Create a cancelable context for the second goroutine
	ctx, cancel := context.WithCancel(mainCtx)
	go worker(ctx, 2)

	// Let the second worker run for 10 seconds
	time.Sleep(10 * time.Second)

	// Cancel the context to signal the second worker to stop
	fmt.Println("Main: sending cancellation signal to worker 2")
	cancel()

	// Give the second worker time to clean up
	time.Sleep(1 * time.Second)

	fmt.Println("Main: all done")
}
