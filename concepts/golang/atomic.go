package main

import (
	"fmt"
	"sync/atomic"
	"time"
)

// Atomic operations are useful for low-level synchronization and for ensuring that certain operations are performed atomically without interference from concurrent goroutines.

func main() {
	var counter int64 // Atomic counter

	// Start multiple goroutines to increment the counter concurrently
	for i := 0; i < 10; i++ {
		go func() {
			for {
				// Atomically increment the counter by 1
				atomic.AddInt64(&counter, 1)
				time.Sleep(time.Millisecond * 100) // Sleep for 100 milliseconds
			}
		}()
	}

	// Wait for a while to allow goroutines to execute
	time.Sleep(time.Second * 1)

	// Atomically load the current value of the counter
	finalCount := atomic.LoadInt64(&counter)
	fmt.Println("Final Counter Value:", finalCount)
}
