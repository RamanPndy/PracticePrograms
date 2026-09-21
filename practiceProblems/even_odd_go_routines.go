package main

import "fmt"

func main() {
	odd := make(chan struct{})
	even := make(chan struct{})
	done := make(chan struct{})

	go func() {
		for i := 1; i <= 9; i += 2 {
			<-odd
			fmt.Println(i)
			even <- struct{}{}
		}
	}()

	go func() {
		for i := 2; i <= 10; i += 2 {
			<-even
			fmt.Println(i)

			if i == 10 {
				close(done)
				return
			}

			odd <- struct{}{}
		}
	}()

	// Kick-start odd goroutine
	odd <- struct{}{}

	// Wait until even goroutine finishes
	<-done
}
