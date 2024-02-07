import threading
import time

class ConcurrencyRateLimiter:
    '''
    Implementing a concurrency rate limiter involves controlling 
    the number of concurrent requests allowed at any given time. 
    One approach is to use a semaphore, which is a synchronization primitive 
    that controls access to a shared resource.

    max_concurrency which specifies the maximum number of concurrent requests allowed.
    allow_request method attempts to acquire a semaphore.
    If the semaphore is available (i.e., the maximum concurrency limit has not been reached), 
    the request is allowed, and True is returned. 
    Otherwise, False is returned, indicating that the request is rate-limited.

    release_request method releases the semaphore when the request processing is complete, 
    allowing other requests to proceed.

    This implementation ensures that the number of concurrent requests does not 
    exceed the specified limit, effectively rate-limiting the concurrency level. 
    Adjusting the max_concurrency parameter allows you to control the concurrency rate limiting 
    behavior according to your requirements.
    '''
    def __init__(self, max_concurrency):
        self.max_concurrency = max_concurrency
        self.semaphore = threading.Semaphore(max_concurrency)

    def allow_request(self):
        if self.semaphore.acquire(blocking=False):
            # Execute the request if the semaphore is acquired
            return True
        else:
            # The maximum concurrency limit has been reached
            return False

    def release_request(self):
        self.semaphore.release()

# Example usage:
rate_limiter = ConcurrencyRateLimiter(max_concurrency=5)

def make_request(request_number):
    if rate_limiter.allow_request():
        print(f"Request {request_number}: Allowed")
        # Simulate some processing time for the request
        time.sleep(1)
        rate_limiter.release_request()
    else:
        print(f"Request {request_number}: Rate limited")

# Simulate making 10 requests concurrently
threads = []
for i in range(10):
    thread = threading.Thread(target=make_request, args=(i + 1,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
