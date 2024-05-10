package main

// the sync.Map type provides a concurrency-safe map for use in concurrent programs.
// It's designed to be efficient and safe for multiple goroutines to read and write to the map concurrently without requiring external synchronization.

// The sync.Map type provides the following methods for managing the map:

// Load(key interface{}) (value interface{}, ok bool): Loads a value for a key from the map.
// Store(key, value interface{}): Stores a value for a key in the map.
// Delete(key interface{}): Deletes a key from the map.
// Range(f func(key, value interface{}) bool): Iterates over all key-value pairs in the map, calling the provided function f for each pair.
// The iteration continues until f returns false.
// sync.Map is a good choice when you need a concurrent map that can be safely accessed by multiple goroutines without external
// synchronization. However, note that sync.Map is less efficient than a regular map (map[KeyType]ValueType) for single-threaded use cases.

import (
	"fmt"
	"sync"
)

func main() {
	// Create a new sync.Map
	var m sync.Map

	// Add key-value pairs to the map
	m.Store("key1", "value1")
	m.Store("key2", "value2")
	m.Store("key3", "value3")

	// Load a value from the map
	if val, ok := m.Load("key1"); ok {
		fmt.Println("Value for key1:", val)
	}

	// Delete a key from the map
	m.Delete("key2")

	// Range over all key-value pairs in the map
	m.Range(func(key, value interface{}) bool {
		fmt.Printf("Key: %v, Value: %v\n", key, value)
		return true // Continue iteration
	})
}
