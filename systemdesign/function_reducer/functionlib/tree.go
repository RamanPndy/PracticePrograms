package functionlib

import "sync"

/*
Explanation
TreeNode: Represents a node in the function tree. Each node has a function and a list of child nodes.
FunctionProcessor: Struct that holds the root node of the function tree and the reduce function.
NewFunctionProcessor: Constructor function for FunctionProcessor.
processNode: Recursively applies the function at the current node and its children, collecting the results and applying the reduce function.
Process: Applies the function tree starting from the root node and returns the reduced result.
Example Functions: add and multiply are example functions.
Example Reduce Function: sum is an example reduce function that sums the results.
Main Application: Demonstrates creating a tree of functions, processing arguments, and printing the result.
*/

// TwoArgFunc is a function type that accepts two arguments and returns an output
type TwoArgFunc func(arg1, arg2 interface{}) interface{}

// ReduceFunc is a function type that takes a list of outputs and returns a single result
type ReduceFunc func(results []interface{}) interface{}

// TreeNode represents a node in the function tree
type TreeNode struct {
	Func     TwoArgFunc
	Children []*TreeNode
}

// FunctionProcessor struct holds the root node of the function tree and the reduce function
type FunctionProcessor struct {
	rootNode *TreeNode
	reduceFn ReduceFunc
}

// NewFunctionProcessor creates a new FunctionProcessor
func NewFunctionProcessor(rootNode *TreeNode, reduceFn ReduceFunc) *FunctionProcessor {
	return &FunctionProcessor{rootNode: rootNode, reduceFn: reduceFn}
}

// processNode applies the function at the current node and recursively processes its children
func (fp *FunctionProcessor) processNode(node *TreeNode, arg1, arg2 interface{}) interface{} {
	if node == nil {
		return nil
	}

	var wg sync.WaitGroup
	results := make([]interface{}, len(node.Children)+1)
	results[0] = node.Func(arg1, arg2)

	for i, child := range node.Children {
		wg.Add(1)
		go func(i int, child *TreeNode) {
			defer wg.Done()
			results[i+1] = fp.processNode(child, arg1, arg2)
		}(i, child)
	}

	wg.Wait()
	return fp.reduceFn(results)
}

// Process applies the function tree to the given arguments and then applies the reduce function
func (fp *FunctionProcessor) Process(arg1, arg2 interface{}) interface{} {
	return fp.processNode(fp.rootNode, arg1, arg2)
}
