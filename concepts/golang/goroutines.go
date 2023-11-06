// These Go routines are managed by go runtime and not by OS. The Goroutines have a similar state like threads- Runnable, running, terminated/done. Like OS threads, goroutines will be used for concurrency.
// a new goroutine will have a stack of only about 4KB. With 4KB per stack, you can put 0.25 million goroutines in a gigabyte of
// RAM – a huge improvement over Java’s 1MB per thread.

// Golang implements its own scheduler that allows many Goroutines to run on the same OS thread. Even if Go ran the same context switching code as the kernel,
// it would save a significant amount of time by avoiding the need to switch into ring-0 to run the kernel and back again.

// If a goroutine is waiting on a empty channel, the scheduler can see that and it won’t run the Goroutine. Go goes one step further and actually sticks the mostly-idle goroutines on their own operating system thread. This way the (hopefully much smaller) number of active goroutines can be scheduled by one thread while the millions of mostly-sleeping goroutines can be tended to separately. This helps keep latency down.

// Why Go routines:

// Lightweight. Goroutines are very small than threads which is 2KB and they increase the stack size when needed (growable segmented stacks), wherein threads the size is ≥1 which is a lot higher when compared to Goroutines.
// OS thread creation and tear down can take more time than goroutine.
// The threads runtime and schedules are maintained by OS, where the context switching of threads would take more time. And the scheduling of threads are preemptive (the thread scheduling will be based on time and priority and this could lead to chance that the task running on the particular thread will take more time because it was context switched at the end of thread function with another thread)
// In Go routines, the scheduling is managed by Go runtime, which follows cooperative scheduling. In cooperative scheduling, the current goroutines will be context switched only if the current goroutines is blocked or done.

// Structs used in the process of scheduling:
// 1. G struct- which holds information about the Go Routines (id, stack and cache and program counter) basically the goroutine details.
// 2. M struct- which points to the OS thread. It has a pointer to the Global queue of runnable Go routines, running Go routine and scheduler.
// 3. Sched struct- contains all the free queues, waiting Go routines and threads

package main

import (
	"net/http"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	var urls = []string{
		"http://www.golang.org/",
		"http://www.google.com/",
		"http://www.somestupidname.com/",
	}
	for _, url := range urls {
		// Increment the WaitGroup counter.
		wg.Add(1)
		// Launch a goroutine to fetch the URL.
		go func(url string) {
			// Decrement the counter when the goroutine completes.
			defer wg.Done()
			// Fetch the URL.
			http.Get(url)
		}(url)
	}
	// Wait for all HTTP fetches to complete.
	wg.Wait()
}

func main() {
	c := make(chan struct{}) // We don't need any data to be passed, so use an empty struct
	for i := 0; i < 100; i++ {
		go func() {
			doSomething()
			c <- struct{}{} // signal that the routine has completed
		}()
	}

	// Since we spawned 100 routines, receive 100 messages.
	for i := 0; i < 100; i++ {
		<-c
	}
}
