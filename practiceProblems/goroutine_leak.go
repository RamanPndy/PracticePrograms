package practiceproblems

/*
Goroutine leak example in Go
Suppose doWork() takes 10 seconds.
After one second:
select
 │
 └── timeout
       ↓
    return
But the goroutine is still running.
After 10 seconds:
goroutine
    ↓
result <- err
Nobody is receiving anymore.

Because result is unbuffered, the goroutine can become permanently blocked.

That's a goroutine leak.
*/

import (
	"errors"
	"time"
)

func process() error {
	result := make(chan error)

	go func() {
		result <- doWork()
	}()

	select {
	case err := <-result:
		return err

	case <-time.After(time.Second):
		return errors.New("timeout")
	}
}
