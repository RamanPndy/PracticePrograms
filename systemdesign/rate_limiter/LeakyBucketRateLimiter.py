# Rate Limiter - an interface - which will be filter the request
# Bucket Creator - will create bucket for each user
# components should be thread safe because multiple requests can come in parallel
import BlockingQueue
import RateLimiterInterface

class LeakyBucket(RateLimiterInterface):
    def __init__(self, capacity) -> None:
        super().__init__()
        self.queue = BlockingQueue(capacity)

    def grantAccess(self):
        super().grantAccess()
        if self.queue.curr_size > 0:
            self.queue.enqueue(1) #accepting one request at a time
            return True
        return False

class UserBucketCreator:
    def __init__(self, id) -> None:
        self.bucket = dict() # Map of int, LeakyBucket
        self.bucket[id] = LeakyBucket(10)

    def accessApplication(self, id):
        if id in self.bucket and self.bucket[id].grantAccess():
            print ("able to access application")
        else:
            print("Too many request, please try after sometime")


userBucketCreator = UserBucketCreator(1)

import time

class LeakyBucketRateLimiter:
    '''
    A leaky bucket rate limiter is a common algorithm used for rate limiting requests in distributed systems.
    capacity represents the maximum number of tokens the bucket can hold
    rate is the rate at which tokens are added to the bucket per second
    interval is the time interval in seconds

    The allow_request method checks if there are enough tokens in the bucket to allow a request. 
    If there are enough tokens, it decrements the token count by 1 and returns True, 
    indicating that the request is allowed. 
    Otherwise, it returns False, indicating that the request is rate-limited.

    This implementation ensures that the rate limiting is applied uniformly over time, 
    preventing sudden bursts of traffic from overwhelming the system while still allowing 
    occasional bursts of requests within the capacity of the bucket. 
    '''
    def __init__(self, capacity, rate, interval):
        self.capacity = capacity  # Maximum number of tokens the bucket can hold
        self.rate = rate  # Rate at which tokens are added to the bucket per second
        self.interval = interval  # Time interval in seconds
        self.tokens = 0  # Current number of tokens in the bucket
        self.last_refresh_time = time.time()  # Last time the bucket was refreshed

    def allow_request(self):
        # Calculate the time elapsed since the last refresh
        current_time = time.time()
        time_elapsed = current_time - self.last_refresh_time
        
        # Refill the bucket with tokens based on the elapsed time
        self.tokens = min(self.capacity, self.tokens + time_elapsed * self.rate)
        
        # Update the last refresh time
        self.last_refresh_time = current_time
        
        # Check if there are enough tokens to allow the request
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

# Example usage:
rate_limiter = LeakyBucketRateLimiter(capacity=10, rate=2, interval=1)

for i in range(15):
    if rate_limiter.allow_request():
        print(f"Request {i + 1}: Allowed")
    else:
        print(f"Request {i + 1}: Rate limited")

    # Simulate some delay between requests
    time.sleep(0.5)
