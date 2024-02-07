import time
import RateLimiterInterface
class TokenBucket(RateLimiterInterface):
    def __init__(self, bucketCapactiy, refreshRate) -> None:
        super().__init__()
        self.bucketCapacity = bucketCapactiy
        self.refreshRate = refreshRate
        self.currentCapactiy = bucketCapactiy
        self.lastUpdatedTime = time.nowInMillis()

    def grantAccess(self):
        self.refreshBucket()
        if self.currentCapactiy > 0:
            self.currentCapactiy -= 1
            return True
        return False
    
    def refreshBucket(self):
        currentTime = time.nowInMillis()
        additionalToken = (currentTime - self.lastUpdatedTime) / 1000 * self.refreshRate
        currCapacity = min(self.currentCapactiy + additionalToken, self.bucketCapacity)
        self.currentCapactiy = currCapacity
        self.lastUpdatedTime = currentTime


class UserBucketCreator:
    def __init__(self, id) -> None:
        self.bucket = dict() # Map of int, TokenBucket
        self.bucket[id] = TokenBucket(10, 10)

    def accessApplication(self, id):
        if id in self.bucket and self.bucket[id].grantAccess():
            print ("able to access application")
        else:
            print("Too many request, please try after sometime")

import time

class TokenBucketRateLimiter:
    '''
    capacity attribute representing the maximum number of tokens the bucket can hold 
    rate attribute representing the rate at which tokens are added to the bucket per second
    tokens attribute tracks the current number of tokens in the bucket
    last_refill_time tracks the last time the bucket was refilled.

    refill_bucket method calculates the number of tokens to add to the bucket based 
    on the elapsed time since the last refill and updates the tokens attribute accordingly.

    allow_request method checks if there are enough tokens in the bucket to allow a request. 
    If there are enough tokens, it decrements the token count by 1 and returns True, 
    indicating that the request is allowed. 
    Otherwise, it returns False, indicating that the request is rate-limited.

    This implementation ensures that the rate limiting is applied uniformly over time, 
    allowing requests at a steady rate within the capacity of the bucket. 
    Adjusting the capacity and rate parameters allows you to control the rate limiting 
    behavior according to your requirements.

    '''
    def __init__(self, capacity, rate):
        self.capacity = capacity  # Maximum number of tokens the bucket can hold
        self.rate = rate  # Rate at which tokens are added to the bucket per second
        self.tokens = capacity  # Current number of tokens in the bucket
        self.last_refill_time = time.time()  # Last time the bucket was refilled

    def refill_bucket(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_refill_time
        tokens_to_add = time_elapsed * self.rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_time = current_time

    def allow_request(self):
        self.refill_bucket()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

# Example usage:
rate_limiter = TokenBucketRateLimiter(capacity=10, rate=2)

for i in range(15):
    if rate_limiter.allow_request():
        print(f"Request {i + 1}: Allowed")
    else:
        print(f"Request {i + 1}: Rate limited")

    # Simulate some delay between requests
    time.sleep(0.5)
