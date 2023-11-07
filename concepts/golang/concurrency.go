// Pattern 1: For-Select-Done
// The main idea of the for-select-done pattern is to use an infinite for loop to handle events from various channels using the
// select statement.

package main

import (
	"context"
	"errors"
	"fmt"
	"math/rand"
	"os"
	"os/signal"
	"sync"
	"syscall"
	"time"

	"golang.org/x/sync/errgroup"
)

// someTask function that we call periodically.
func someTask() {
	fmt.Println(rand.Int() * rand.Int())
}

// PeriodicTask runs someTask every 1 second.
// If canceled goroutine should be stopped.
func PeriodicTask(ctx context.Context) {
	// Create a new ticker with a period of 1 second.
	ticker := time.NewTicker(time.Second)
	for {
		select {
		case <-ticker.C:
			someTask()
		case <-ctx.Done():
			fmt.Println("stopping PeriodicTask")
			ticker.Stop()
			return
		}
	}
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	go PeriodicTask(ctx)

	// Create a channel to receive signals from the operating system.
	sigCh := make(chan os.Signal, 1)
	signal.Notify(sigCh, syscall.SIGTERM)

	// The code blocks until a signal is received (e.g. Ctrl+C).
	<-sigCh
}

// Pattern 2: Errgroup
// The main idea of the errgroup pattern is to start a group of goroutines, wait for them to finish their work,
// and handle any errors that may occur during execution.

// errFailure some custom error.
var errFailure = errors.New("some error")

func main() {
	// Create errgroup.
	group := errgroup.Group{}

	// Run first task.
	group.Go(func() error {
		time.Sleep(5 * time.Second)
		fmt.Println("doing some work 1")
		return nil
	})

	// Run second task.
	group.Go(func() error {
		fmt.Println("doing some work 2")
		return nil
	})

	// Run third task.
	group.Go(func() error {
		fmt.Println("doing some work 3")
		return errFailure
	})

	// Wait for all goroutines to complete.
	if err := group.Wait(); err != nil {
		fmt.Printf("errgroup tasks ended up with an error: %v\n", err)
	} else {
		fmt.Println("all works done successfully")
	}
}

// Pattern 3: Worker Pool
// The worker pool pattern is a pattern that allows tasks to be parallelized, limiting the number of simultaneously executing goroutines.

var taskCount = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

const (
	// Number of concurrent workers.
	numberOfWorkers = 3
)

func main() {
	// Create buffered channel.
	jobs := make(chan struct{}, numberOfWorkers)
	wg := sync.WaitGroup{}

	// Add workers.
	for id := range taskCount {
		wg.Add(1)
		jobs <- struct{}{}

		go func(id int) {
			worker(id)
			<-jobs
			defer wg.Done()
		}(id)
	}

	// Wait for all workers to complete.
	wg.Wait()
}

func worker(id int) {
	fmt.Println(id)
	time.Sleep(2 * time.Second)
}
