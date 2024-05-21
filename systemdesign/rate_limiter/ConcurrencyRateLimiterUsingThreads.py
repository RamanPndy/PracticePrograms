import threading
import time

class ConcurrencyRateLimiter:
    '''
    Implementing a concurrency rate limiter in Python involves limiting the number of 
    concurrent requests or operations that can be executed simultaneously.

    max_concurrency which specifies the maximum number of concurrent executions allowed.

    execute method is used to execute a function while respecting the concurrency limit. 
    It acquires a lock to ensure thread safety and checks if the 
    current concurrency exceeds the limit. 
    If it does, the method returns False. 
    Otherwise, it increments the current concurrency count and executes the provided function. 
    After execution, it decrements the concurrency count.

    task function simulates a task by printing messages and sleeping for a short period. 
    You can replace it with any function you want to execute concurrently.

    Example usage demonstrates creating multiple threads to execute tasks concurrently, 
    each wrapped with the rate limiter.

    This concurrency rate limiter ensures that the maximum number of concurrent executions is not exceeded, 
    thus preventing resource exhaustion or overload. 
    Adjusting the max_concurrency parameter allows you to control the concurrency limit according to your requirements.
    '''
    def __init__(self, max_concurrency):
        self.max_concurrency = max_concurrency
        self.lock = threading.Lock()
        self.current_concurrency = 0

    def execute(self, func):
        with self.lock:
            if self.current_concurrency >= self.max_concurrency:
                return False

            self.current_concurrency += 1

        try:
            result = func()
            return result
        finally:
            with self.lock:
                self.current_concurrency -= 1

# Example usage:
def task():
    print("Executing task...")
    time.sleep(1)
    print("Task executed.")
    return "Task result"

limiter = ConcurrencyRateLimiter(max_concurrency=2)

# Try to execute tasks concurrently
threads = []
for i in range(5):
    thread = threading.Thread(target=lambda: limiter.execute(task))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
