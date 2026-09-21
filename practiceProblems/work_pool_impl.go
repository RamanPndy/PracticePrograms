package main

/*
Worker pool implementation in Go
Implement a worker pool in Go that processes N jobs using a fixed number of workers.
The number of workers should be configurable, and the main function should wait until all jobs are completed.
*/

import (
	"fmt"
	"time"
)

type Job struct {
	ID int
}

func worker(id int, jobs <-chan Job, done chan<- struct{}) {
	for job := range jobs {
		fmt.Printf("Worker %d processing Job %d\n", id, job.ID)

		time.Sleep(500 * time.Millisecond)

		fmt.Printf("Worker %d completed Job %d\n", id, job.ID)
	}

	done <- struct{}{}
}

func main() {
	const (
		numWorkers = 3
		numJobs    = 10
	)

	jobs := make(chan Job)
	done := make(chan struct{}, numWorkers)

	// Start workers
	for i := 1; i <= numWorkers; i++ {
		go worker(i, jobs, done)
	}

	// Submit jobs
	go func() {
		for i := 1; i <= numJobs; i++ {
			jobs <- Job{ID: i}
		}

		close(jobs)
	}()

	// Wait for workers
	for i := 0; i < numWorkers; i++ {
		<-done
	}

	fmt.Println("All jobs completed")
}
