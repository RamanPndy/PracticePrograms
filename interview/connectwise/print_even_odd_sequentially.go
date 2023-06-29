package main

import (
	"fmt"
	"sync"
)

func printEven(wg *sync.WaitGroup) {
	defer wg.Done()

	for i := 0; i <= 10; i += 2 {
		fmt.Println("Even:", i)
	}
}

func printOdd(wg *sync.WaitGroup) {
	defer wg.Done()

	for i := 1; i <= 10; i += 2 {
		fmt.Println("Odd:", i)
	}
}

func main() {
	var wg sync.WaitGroup
	wg.Add(2)

	go printEven(&wg)
	go printOdd(&wg)

	wg.Wait()
}
