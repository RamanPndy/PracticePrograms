package main

import (
	"fmt"
	"sync"
)

func printEven(wg *sync.WaitGroup, evenChan chan<- int) {
	defer wg.Done()
	for i := 2; i <= 10; i += 2 {
		evenChan <- i // Send even number to evenChan
	}
	close(evenChan) // Close the channel when done
}

func printOdd(wg *sync.WaitGroup, evenChan <-chan int) {
	defer wg.Done()
	for num := range evenChan {
		fmt.Println("Even:", num)
		fmt.Println("Odd:", num-1)
	}
}

func main() {
	var wg sync.WaitGroup
	evenChan := make(chan int)

	wg.Add(2)
	go printEven(&wg, evenChan)
	go printOdd(&wg, evenChan)

	wg.Wait() // Wait for goroutines to finish
}
