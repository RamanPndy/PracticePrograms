Role of init function
In Go, the "init" function is a special function that is automatically called by the Go runtime when a package is initialized. It is called before the main function and can be used to perform initialization tasks for the package.

The "init" function does not take any arguments and does not return a value. It is typically used to set initial values for package-level variables, establish connections to external resources such as databases, or perform any other initialization tasks that need to be performed before the main function is called.

The "init" function can be defined anywhere in the package, and multiple "init" functions can be defined in the same package. All "init" functions within a package will be called by the Go runtime in the order they appear in the code.

The "init" function is a useful tool for performing initialization tasks that need to be done before the main function is called, and it is often used in conjunction with the "main" package to set up the environment for the main function to run. 

Difference between array and slice
array is value type and slice is reference type

You can see clearly that the array is over 10 times faster than the slice.

var a [5]int 
an array of integers with a length of 5

a := make([]int, 5) 
This creates a slice with a length of 5 and a capacity of 5. 
One important difference between arrays and slices is that arrays are value types, whereas slices are reference types. 
This means that when you pass an array to a function or assign it to a new variable, a copy of the array is made. 
On the other hand, when you pass a slice to a function or assign it to a new variable, only a reference to the underlying array is copied. 
This can be important to consider when working with large arrays or when you want to avoid copying data unnecessarily.

Goroutine leaks
More specifically, for an unbuffered channel, the sender blocks until the receiver arrives at the channel and vice versa. A goroutine may be blocked forever trying to send or receive on a channel; such a situation where a blocked goroutine never gets unblocked is referred to as a goroutine leak.

function Closure
In Go, a function closure is a function that refers to variables from the scope in which it was defined. 
These variables are "closed over" by the function, and they remain accessible even after the function is invoked outside of their original scope. 
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

reflect in golang
To inspect the type of a variable, you can use the reflect.TypeOf() function. This function takes an interface{} value and returns a reflect.Type value representing the type of the underlying value.
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

difference between new and make
In summary, new is used to allocate memory for a new value of a specified type and return a pointer to that memory, 
while make is used to create a new instance of a reference type and initialize it to a non-zero value. 
Both new and make are useful for creating new values in Go, depending on the situation.

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

Difference between new() and make():
new(T) allocates zeroed storage for a new item of type T and returns its address, a value of type *T: it returns a pointer to a newly allocated zero value of type T, ready for use; it applies to value types like arrays and structs; it is equivalent to &T{ }
make(T) returns an initialized value of type T; it applies only to the 3 built-in reference types: slices, maps and channels.
In other words, new allocates; make initializes;

var p *[]int = new([]int)
or
// *p == nil; with len and cap 0
p := new([]int)
which is only rarely useful.

p := make([]int, 0)
our slice is initialized, but here points to an empty array.

Both these statements aren't very useful, the following is:

var v []int = make([]int, 10, 50)
// Or
v := make([]int, 10, 50)
This allocates an array of 50 ints and then creates a slice v with length 10 and capacity 50 pointing to the first 10 elements of the array.

Find out some rules for make() and new():
For slices, maps and channels: use make
For arrays, structs and all value types: use new
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

Rune literals are just 32-bit integer values (however they're untyped constants, so their type can change). They represent unicode codepoints. For example, the rune literal 'a' is actually the number 97.

Therefore your program is pretty much equivalent to:

package main

import "fmt"

func SwapRune(r rune) rune {
    switch {
    case 97 <= r && r <= 122:
        return r - 32
    case 65 <= r && r <= 90:
        return r + 32
    default:
        return r
    }
}

func main() {
    fmt.Println(SwapRune('a'))
}
It should be obvious, if you were to look at the Unicode mapping, which is identical to ASCII in that range. Furthermore, 32 is in fact the offset between the uppercase and lowercase codepoint of the character. So by adding 32 to 'A', you get 'a' and vice versa.