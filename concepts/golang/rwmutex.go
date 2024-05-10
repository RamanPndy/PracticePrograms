package main

import (
	"fmt"
	"sync"
	"time"
)

// SharedData represents a shared resource.
type SharedData struct {
	data map[string]int
	mu   sync.RWMutex
}

// NewSharedData creates a new instance of SharedData.
func NewSharedData() *SharedData {
	return &SharedData{
		data: make(map[string]int),
	}
}

// ReadData reads the data using a read lock.
func (sd *SharedData) ReadData(key string) int {
	sd.mu.RLock()
	defer sd.mu.RUnlock()
	return sd.data[key]
}

// WriteData writes data using a write lock.
func (sd *SharedData) WriteData(key string, value int) {
	sd.mu.Lock()
	defer sd.mu.Unlock()
	sd.data[key] = value
}

func main() {
	// Create a new instance of SharedData
	data := NewSharedData()

	// Concurrently read and write data
	go func() {
		for i := 0; i < 10; i++ {
			data.WriteData(fmt.Sprintf("key%d", i), i)
			time.Sleep(time.Millisecond * 100)
		}
	}()

	go func() {
		for i := 0; i < 10; i++ {
			key := fmt.Sprintf("key%d", i)
			value := data.ReadData(key)
			fmt.Printf("Read: %s - Value: %d\n", key, value)
			time.Sleep(time.Millisecond * 50)
		}
	}()

	// Wait for goroutines to finish
	time.Sleep(time.Second)
}
