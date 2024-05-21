import time

class BurstyRateLimiter:
    '''
    A bursty rate limiter allows occasional bursts of requests 
    while still enforcing an overall rate limit over time. 
    One way to implement this is by combining a token bucket 
    with a fixed window approach.

    refill_bucket method is responsible for refilling the token bucket over time
    similar to the token bucket rate limiter.

    allow_request method checks if there are enough tokens in the bucket to allow a request, 
    and also checks if the number of requests made within the window is below the maximum limit, 
    similar to the fixed window rate limiter.

    Requests outside the current window are removed from the request_times list to 
    keep track of only the requests within the window.

    This implementation allows occasional bursts of requests while still enforcing 
    an overall rate limit over time. Adjusting the parameters (capacity, rate, window_size, max_requests) 
    allows you to control the burstiness and rate limiting behavior according to your requirements.
    '''
    def __init__(self, capacity, rate, window_size, max_requests):
        self.capacity = capacity  # Maximum number of tokens the bucket can hold
        self.rate = rate  # Rate at which tokens are added to the bucket per second
        self.tokens = capacity  # Current number of tokens in the bucket
        self.last_refill_time = time.time()  # Last time the bucket was refilled
        self.window_size = window_size  # Time window in seconds
        self.max_requests = max_requests  # Maximum number of requests allowed in the window
        self.request_times = []  # List to store timestamps of requests

    def refill_bucket(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_refill_time
        tokens_to_add = time_elapsed * self.rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_time = current_time

    def allow_request(self):
        self.refill_bucket()

        # Remove requests that fall outside the current window
        current_time = time.time()
        self.request_times = [t for t in self.request_times if t > current_time - self.window_size]

        # Check if the number of requests within the window exceeds the limit
        if len(self.request_times) < self.max_requests:
            # Check if there are enough tokens in the bucket
            if self.tokens >= 1:
                self.tokens -= 1
                self.request_times.append(current_time)
                return True
            else:
                return False
        else:
            return False

# Example usage:
rate_limiter = BurstyRateLimiter(capacity=10, rate=2, window_size=10, max_requests=5)

for i in range(15):
    if rate_limiter.allow_request():
        print(f"Request {i + 1}: Allowed")
    else:
        print(f"Request {i + 1}: Rate limited")

    # Simulate some delay between requests
    time.sleep(1)
