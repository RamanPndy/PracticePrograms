package main

import (
	"fmt"
)

func printEven(done chan<- bool) {
	for i := 0; i <= 10; i += 2 {
		fmt.Println("Even:", i)
	}
	done <- true
}

func printOdd(done chan<- bool) {
	for i := 1; i <= 10; i += 2 {
		fmt.Println("Odd:", i)
	}
	done <- true
}

func main() {
	done := make(chan bool)

	go printEven(done)
	go printOdd(done)

	<-done
	<-done
}
