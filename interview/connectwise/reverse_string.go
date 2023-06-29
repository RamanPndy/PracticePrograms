package main

import "fmt"

func reverseString(str string) string {
	runes := []rune(str)
	length := len(runes)

	// Swap characters from both ends
	for i, j := 0, length-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	return string(runes)
}

func main() {
	str := "Hello, World!"
	reversed := reverseString(str)
	fmt.Println(reversed)
}
