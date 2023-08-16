// insert value at specific index
func insert(a []int, index int, value int) []int {
	if len(a) == index { // nil or empty slice or after last element
		return append(a, value)
	}
	a = append(a[:index+1], a[index:]...) // index < len(a)
	a[index] = value
	return a
}

// function Closure
// In Go, a function closure is a function that refers to variables from the scope in which it was defined. 
// These variables are "closed over" by the function, and they remain accessible even after the function is invoked outside of their original scope. 
package main 
import "fmt" 
func main() { 
// Create a variable x and initialize it to 10 
x := 10 
// Create a function closure that captures the value of x 
addX := func(y int) int { 
    return x + y 
} 
// Use the function closure to add x to different values of y 
fmt.Println(addX(5))  // prints 15 
fmt.Println(addX(10)) // prints 20 
// Modify the value of x and see that the function closure still uses the original value 
x = 20 
fmt.Println(addX(5))  // still prints 15 
} 

// reflect in golang
// To inspect the type of a variable, you can use the reflect.TypeOf() function. This function takes an interface{} value and returns a reflect.Type value representing the type of the underlying value.
package main 
import ( 
"fmt" 
"reflect" 
) 
func main() { 
var x int = 10 
fmt.Println(reflect.TypeOf(x)) // prints "int" 
var y float64 = 3.14 
fmt.Println(reflect.TypeOf(y)) // prints "float64" 
var z string = "hello" 
fmt.Println(reflect.TypeOf(z)) // prints "string" 
} 

// difference between new and make
// In summary, new is used to allocate memory for a new value of a specified type and return a pointer to that memory, 
// while make is used to create a new instance of a reference type and initialize it to a non-zero value. 
// Both new and make are useful for creating new values in Go, depending on the situation.

func main() {
    fmt.Println("-- MAKE --")
    a := make([]int, 0)
    aPtr := &a
    fmt.Println("pointer == nil :", *aPtr == nil)
    fmt.Printf("pointer value: %p\n\n", *aPtr)

    fmt.Println("-- COMPOSITE LITERAL --")
    b := []int{}
    bPtr := &b
    fmt.Println("pointer == nil :", *bPtr == nil)
    fmt.Printf("pointer value: %p\n\n", *bPtr)

    fmt.Println("-- NEW --")
    cPtr := new([]int)
    fmt.Println("pointer == nil :", *cPtr == nil)
    fmt.Printf("pointer value: %p\n\n", *cPtr)

    fmt.Println("-- VAR (not initialized) --")
    var d []int
    dPtr := &d
    fmt.Println("pointer == nil :", *dPtr == nil)
    fmt.Printf("pointer value: %p\n", *dPtr)
}

output 
-- MAKE --
pointer == nil : false
pointer value: 0x118eff0  # address to underlying array

-- COMPOSITE LITERAL --
pointer == nil : false
pointer value: 0x118eff0  # address to underlying array

-- NEW --
pointer == nil : true
pointer value: 0x0

-- VAR (not initialized) --
pointer == nil : true
pointer value: 0x0

// Difference between new() and make():
// new(T) allocates zeroed storage for a new item of type T and returns its address, a value of type *T: it returns a pointer to a newly allocated zero value of type T, ready for use; it applies to value types like arrays and structs; it is equivalent to &T{ }
// make(T) returns an initialized value of type T; it applies only to the 3 built-in reference types: slices, maps and channels.
// In other words, new allocates; make initializes;

var p *[]int = new([]int)
or
// *p == nil; with len and cap 0
p := new([]int)
which is only rarely useful.

enter image description here

p := make([]int, 0)
// our slice is initialized, but here points to an empty array.

// Both these statements aren't very useful, the following is:

var v []int = make([]int, 10, 50)
// Or
v := make([]int, 10, 50)
// This allocates an array of 50 ints and then creates a slice v with length 10 and capacity 50 pointing to the first 10 elements of the array.

// Find out some rules for make() and new():
// For slices, maps and channels: use make
// For arrays, structs and all value types: use new
package main
type Foo map[string]string
type Bar struct {
         s string
         i int
}
func main() {
         // OK:
         y := new(Bar)
         (*y).s = "hello"
         (*y).i = 1

         // NOT OK:
         z := make(Bar) // compile error: cannot make type Bar
         z.s = "hello"
         z.i = 1

         // OK:
         x := make(Foo)
         x["x"] = "goodbye"
         x["y"] = "world"

         // NOT OK:
         u := new(Foo)
         (*u)["x"] = "goodbye" // !!panic!!: runtime error: 
                   // assignment to entry in nil map
         (*u)["y"] = "world"
}