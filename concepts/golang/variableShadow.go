package main

// Variable shadowing in Go occurs when a variable declared in a nested block or scope has the same name as a variable in an outer block or scope.
// When this happens, the inner variable "shadows" or hides the outer variable, making the outer variable inaccessible within the inner scope.
// This behavior can sometimes lead to confusion and bugs if not handled carefully.

import "fmt"

func main() {
	x := 10
	fmt.Println("Outer x:", x) // Prints "Outer x: 10"

	if true {
		x := 20
		fmt.Println("Inner x:", x) // Prints "Inner x: 20"
	}

	fmt.Println("Outer x after inner block:", x) // Prints "Outer x after inner block: 10"
}
