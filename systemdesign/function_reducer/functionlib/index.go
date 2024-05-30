package functionlib

import "sync"

// Function type that accepts two arguments and returns an output
type TwoArgFunc func(arg1, arg2 interface{}) interface{}

// Reduce function type that takes a list of outputs and returns a single result
type ReduceFunc func(results []interface{}) interface{}

// FunctionProcessor struct that holds a list of functions and a reduce function
type FunctionProcessor struct {
	funcs    []TwoArgFunc
	reduceFn ReduceFunc
}

// NewFunctionProcessor creates a new FunctionProcessor
func NewFunctionProcessor(funcs []TwoArgFunc, reduceFn ReduceFunc) *FunctionProcessor {
	return &FunctionProcessor{funcs: funcs, reduceFn: reduceFn}
}

// Process applies the list of functions to the given arguments and then applies the reduce function
func (fp *FunctionProcessor) Process(arg1, arg2 interface{}) interface{} {
	var wg sync.WaitGroup
	results := make([]interface{}, len(fp.funcs))

	for i, fn := range fp.funcs {
		wg.Add(1)
		go func(i int, fn TwoArgFunc) {
			defer wg.Done()
			results[i] = fn(arg1, arg2)
		}(i, fn)
	}

	wg.Wait()
	return fp.reduceFn(results)
}
