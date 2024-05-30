package main

/*
Time Complexity: O(nlogn)
Algorithm Used: Timsort, a hybrid of merge sort and insertion sort
Functions: sort.Ints, sort.Strings, sort.Float64s, sort.Slice, and others in the sort package
*/

import (
    "fmt"
    "sort"
)

type Person struct {
    Name string
    Age  int
}

func sortIntegers() {
	// Define a slice of integers
    numbers := []int{5, 3, 4, 1, 2}

    // Sort the slice in ascending order
    sort.Ints(numbers)

    // Print the sorted slice
    fmt.Println("Sorted slice:", numbers)

	// Sort the slice in descending order
    sort.Slice(numbers, func(i, j int) bool {
        return numbers[i] > numbers[j]
    })

	// Print the sorted slice
    fmt.Println("Sorted slice in descending order:", numbers)
}

func sortStrings() {
	// Define a slice of strings
	names := []string{"Charlie", "Alice", "Bob", "Eve", "David"}

	// Sort the slice in ascending order
	sort.Strings(names)

	// Print the sorted slice
	fmt.Println("Sorted slice:", names)

	// Sort the slice in descending order
	sort.Slice(names, func(i, j int) bool {
		return names[i] > names[j]
	})

	// Print the sorted slice
	fmt.Println("Sorted slice in descending order:", names)
}

func sortFloats() {
	// Define a slice of float64 numbers
    values := []float64{3.1, 2.4, 1.6, 5.9, 4.3}

    // Sort the slice in ascending order
    sort.Float64s(values)

    // Print the sorted slice
    fmt.Println("Sorted slice:", values)

	// Sort the slice in descending order
    sort.Slice(values, func(i, j int) bool {
        return values[i] > values[j]
    })

    // Print the sorted slice
    fmt.Println("Sorted slice in descending order:", values)
}

func sortStructs() {
	// Define a slice of Person structs
    people := []Person{
        {"Alice", 30},
        {"Bob", 25},
        {"Charlie", 35},
        {"David", 20},
        {"Eve", 28},
    }

    // Sort the slice by the Age field in ascending order
    sort.Slice(people, func(i, j int) bool {
        return people[i].Age < people[j].Age
    })

    // Print the sorted slice
    fmt.Println("Sorted slice by age:", people)

	// Sort the slice by the Age field in descending order
    sort.Slice(people, func(i, j int) bool {
        return people[i].Age > people[j].Age
    })

    // Print the sorted slice
    fmt.Println("Sorted slice by age in descending order:", people)
}

func main() {
	sortIntegers()
	sortStrings()
	sortFloats()
	sortStructs()
}
