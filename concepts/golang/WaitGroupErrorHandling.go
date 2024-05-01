package main

import (
	"errors"
	"fmt"
	"sync"
)

func worker(id int, wg *sync.WaitGroup, errCh chan error) {
	defer wg.Done()

	// Simulating some work
	if id == 2 {
		errCh <- errors.New("error occurred in worker 2")
		return
	}

	fmt.Printf("Worker %d completed\n", id)
}

func main() {
	var wg sync.WaitGroup
	errCh := make(chan error, 1)

	numWorkers := 3
	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go worker(i, &wg, errCh)
	}

	go func() {
		wg.Wait()
		close(errCh)
	}()

	for err := range errCh {
		fmt.Println("Error:", err)
	}

	fmt.Println("All workers completed")
}
