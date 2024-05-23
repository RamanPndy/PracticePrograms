package main

/*
The context package in Go is used to manage deadlines, cancelation signals, and other request-scoped values across API 
boundaries and goroutines. It's particularly useful for controlling the lifecycle of operations and handling 
cancellations gracefully.

Key Concepts
Context: A context is an immutable object that carries deadlines, cancellation signals, and other values across API 
boundaries and between goroutines.

WithCancel: Creates a context that can be canceled.

WithDeadline: Creates a context that will be canceled when a specific time is reached.

WithTimeout: Creates a context that will be canceled after a timeout duration.

WithValue: Creates a context that carries a key-value pair.

Don't pass nil contexts: Always use context.TODO() or context.Background() when unsure.

Contexts are immutable: When you need to derive a new context, always use one of the With* functions.

Cancel contexts to release resources: Always call the cancel function returned by WithCancel, WithTimeout, or 
WithDeadline to avoid resource leaks.

Context should be the first parameter: In functions, the context should be the first parameter, typically named ctx.

Graceful Shutdown: The goroutine can finish its current work before stopping, ensuring a clean shutdown.

Context Propagation: The context can be passed down to other functions or goroutines if needed.

Avoid Resource Leaks: Using context helps in avoiding resource leaks by ensuring goroutines can be stopped when they 
are no longer needed.
*/

import (
    "context"
    "fmt"
    "time"
)

func contextWithCancel() {
    // Create a context that can be canceled
    ctx, cancel := context.WithCancel(context.Background())

    // Simulate a goroutine that does some work and then cancels the context
    go func() {
        time.Sleep(2 * time.Second) // Simulate work
        cancel()
    }()

    // Simulate a worker that checks for context cancelation
    work(ctx)
}

func contextWithTimeout() {
    // Create a context that will be canceled after a timeout
    ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
    defer cancel() // Ensure the context is canceled to release resources

    // Simulate a worker that checks for context cancelation
    work(ctx)
}

func contextWithDeadline() {
    // Create a context that will be canceled at a specific time
    deadline := time.Now().Add(3 * time.Second)
    ctx, cancel := context.WithDeadline(context.Background(), deadline)
    defer cancel() // Ensure the context is canceled to release resources

    // Simulate a worker that checks for context cancelation
    work(ctx)
}

func infiniteWorker(ctx context.Context) {
    for {
        select {
        case <-ctx.Done():
            fmt.Println("Goroutine stopped")
            return
        default:
            // Simulate some work
            fmt.Println("Working...")
            time.Sleep(1 * time.Second)
        }
    }
}

func signalInfiniteGoRoutineToStop() {
    // Create a context with cancelation
    ctx, cancel := context.WithCancel(context.Background())

    // Start the infinite goroutine
    go infiniteWorker(ctx)

    // Simulate some work in the main function
    time.Sleep(5 * time.Second)

    // Signal the goroutine to stop
    cancel()

    // Wait a bit to observe the goroutine stopping
    time.Sleep(1 * time.Second)
}

func main() {
    // Create a context with a value
    ctx := context.WithValue(context.Background(), "key", "value")

    // Retrieve the value from the context
    value := ctx.Value("key")
    if value != nil {
        fmt.Println("Found value:", value)
    } else {
        fmt.Println("Value not found")
    }
}

func work(ctx context.Context) {
    select {
    case <-ctx.Done():
        fmt.Println("Work canceled:", ctx.Err())
    case <-time.After(5 * time.Second):
        fmt.Println("Work completed")
    }
}
