// Using Mutex
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

var (
	mu      sync.Mutex
	counter int
)

func increment() {
	mu.Lock()
	defer mu.Unlock()
	counter++
}

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			increment()
		}()
	}
	wg.Wait()

	fmt.Println("Counter:", counter)
}

// Using channels : Use channels for communication between goroutines to avoid race conditions.
// Channels ensure that only one goroutine has access to the data at any given time.

func increment(counter chan int, done chan bool) {
	for i := 0; i < 1000; i++ {
		counter <- 1
	}
	done <- true
}

func main() {
	counter := make(chan int)
	done := make(chan bool)
	var count int

	go increment(counter, done)

	go func() {
		for {
			select {
			case val := <-counter:
				count += val
			case <-done:
				fmt.Println("Counter:", count)
				return
			}
		}
	}()

	<-done
}

// Using atomic operations :
var counter int64

func increment(wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 0; i < 1000; i++ {
		atomic.AddInt64(&counter, 1)
	}
}

func main() {
	var wg sync.WaitGroup

	for i := 0; i < 100; i++ {
		wg.Add(1)
		go increment(&wg)
	}

	wg.Wait()

	fmt.Println("Counter:", counter)
}
