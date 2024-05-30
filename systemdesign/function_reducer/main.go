package functionreducer

import (
	"fmt"
	"functionlib"
)

// Example functions
func add(a, b interface{}) interface{} {
	return a.(int) + b.(int)
}

func multiply(a, b interface{}) interface{} {
	return a.(int) * b.(int)
}

// Example reduce function
func sum(results []interface{}) interface{} {
	total := 0
	for _, result := range results {
		total += result.(int)
	}
	return total
}

func main() {
	// List of functions
	funcs := []functionlib.TwoArgFunc{add, multiply}

	// Reduce function
	reduceFn := sum

	// Create a FunctionProcessor
	processor := functionlib.NewFunctionProcessor(funcs, reduceFn)

	// Process the arguments and get the result
	result := processor.Process(3, 4)

	// Print the result
	fmt.Println(result) // Output: 19 (3+4 + 3*4)
}

func main() {
	// Creating a tree of functions
	root := &functionlib.TreeNode{
		Func: add,
		Children: []*functionlib.TreeNode{
			{
				Func: multiply,
				Children: []*functionlib.TreeNode{
					{Func: add},
				},
			},
			{
				Func: add,
			},
		},
	}

	// Create a FunctionProcessor with the function tree and reduce function
	processor := functionlib.NewFunctionProcessor(root, sum)

	// Process the arguments and get the result
	result := processor.Process(3, 4)

	// Print the result
	fmt.Println(result) // Output will depend on the tree structure and functions
}
