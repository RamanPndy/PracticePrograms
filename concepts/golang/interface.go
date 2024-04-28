package main

import (
	"fmt"
)

type Person interface {
	Work()
}

type worker string

func (w worker) Work() {
	fmt.Printf("%s is working\n", w)
}

func DoWork[T Person](things []T) {
	for _, v := range things {
		v.Work()
	}
}

func DoWorkInterface(things []Person) {
	for _, v := range things {
		v.Work()
	}
}

func main() {
	var a, b, c, d, e, f worker
	a = "A"
	b = "B"
	c = "C"
	d = "D"
	e = "E"
	f = "F"
	DoWork([]worker{a, b, c})
	DoWorkInterface([]Person{d, e, f})
}
