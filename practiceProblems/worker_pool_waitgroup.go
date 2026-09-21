package main

import (
	"fmt"
	"sync"
)

type Job struct {
	ID int
}

type Result struct {
	JobID int
	Err   error
}

func process(job Job) error {
	fmt.Println("processing job:", job.ID)
	return nil
}

func worker(
	id int,
	jobs <-chan Job,
	results chan<- Result,
	wg *sync.WaitGroup,
) {
	defer wg.Done()

	for job := range jobs {
		err := process(job)

		results <- Result{
			JobID: job.ID,
			Err:   err,
		}
	}
}

func main() {
	const numWorkers = 3
	const numJobs = 10

	jobs := make(chan Job, numJobs)
	results := make(chan Result, numJobs)

	var wg sync.WaitGroup

	wg.Add(numWorkers)

	for i := 1; i <= numWorkers; i++ {
		go worker(i, jobs, results, &wg)
	}

	for i := 1; i <= numJobs; i++ {
		jobs <- Job{ID: i}
	}

	close(jobs)

	wg.Wait()

	close(results)

	for result := range results {
		if result.Err != nil {
			fmt.Printf(
				"job %d failed: %v\n",
				result.JobID,
				result.Err,
			)
		}
	}
}
