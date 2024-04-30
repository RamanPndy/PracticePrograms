package main

import (
	"fmt"

	"github.com/iancoleman/orderedmap"
)

func main() {
	om := orderedmap.New()
	om.Set("c", 3)
	om.Set("a", 1)
	om.Set("b", 2)

	// Iterate over the ordered map
	for _, key := range om.Keys() {
		value, _ := om.Get(key)
		fmt.Println(key, value)
	}
}
