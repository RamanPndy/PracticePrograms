package main

import (
	"fmt"
	"sync"
)

func printEven(wg *sync.WaitGroup, evenCh chan<- int) {
	defer wg.Done()

	for i := 0; i <= 10; i += 2 {
		evenCh <- i
	}
	close(evenCh)
}

func printOdd(wg *sync.WaitGroup, oddCh chan<- int) {
	defer wg.Done()

	for i := 1; i <= 10; i += 2 {
		oddCh <- i
	}
	close(oddCh)
}

func main() {
	evenCh := make(chan int)
	oddCh := make(chan int)
	var wg sync.WaitGroup

	wg.Add(2)
	go printEven(&wg, evenCh)
	go printOdd(&wg, oddCh)

	go func() {
		wg.Wait()
		close(evenCh)
		close(oddCh)
	}()

	for even := range evenCh {
		fmt.Println("Even:", even)
	}

	for odd := range oddCh {
		fmt.Println("Odd:", odd)
	}
}
