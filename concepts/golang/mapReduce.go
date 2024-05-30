package main

/*
Map Function (mapFunc): Takes a string of text, splits it into words, and returns a slice of KeyValue pairs,
where each word is paired with the value 1.
Reduce Function (reduceFunc): Takes a key and a slice of values, and sums up the values, returning the total count for the key.
MapReduce Function (mapReduce):
Runs the map function on each input string in parallel.
Collects the intermediate key-value pairs.
Groups the key-value pairs by key.
Runs the reduce function on each group of values for each key.
Returns a map of keys to their reduced values.
Main Function (main): Defines input data, runs the MapReduce function, and prints the results.
*/

import (
	"fmt"
	"strings"
	"sync"
)

// Map function type
type MapFunc func(string) []KeyValue

// Reduce function type
type ReduceFunc func(string, []int) int

// KeyValue struct to store the key-value pairs emitted by the map function
type KeyValue struct {
	Key   string
	Value int
}

// A simple map function that splits text into words and emits each word with a count of 1
func mapFunc(text string) []KeyValue {
	words := strings.Fields(text)
	kvs := make([]KeyValue, len(words))
	for i, word := range words {
		kvs[i] = KeyValue{Key: word, Value: 1}
	}
	return kvs
}

// A simple reduce function that sums up the counts for each word
func reduceFunc(key string, values []int) int {
	sum := 0
	for _, value := range values {
		sum += value
	}
	return sum
}

// A function to run the MapReduce process
func mapReduce(inputs []string, mapFunc MapFunc, reduceFunc ReduceFunc) map[string]int {
	// Run the map function in parallel and collect intermediate results
	var intermediate []KeyValue
	var mu sync.Mutex
	var wg sync.WaitGroup

	for _, input := range inputs {
		wg.Add(1)
		go func(input string) {
			defer wg.Done()
			kvs := mapFunc(input)
			mu.Lock()
			intermediate = append(intermediate, kvs...)
			mu.Unlock()
		}(input)
	}

	wg.Wait()

	// Group by key
	groups := make(map[string][]int)
	for _, kv := range intermediate {
		groups[kv.Key] = append(groups[kv.Key], kv.Value)
	}

	// Run the reduce function on each group
	outputs := make(map[string]int)
	for key, values := range groups {
		outputs[key] = reduceFunc(key, values)
	}

	return outputs
}

func main() {
	// Input data
	texts := []string{
		"this is a test",
		"this is another test",
		"and another test",
	}

	// Run MapReduce
	result := mapReduce(texts, mapFunc, reduceFunc)

	// Print the results
	for key, value := range result {
		fmt.Printf("%s: %d\n", key, value)
	}
}
