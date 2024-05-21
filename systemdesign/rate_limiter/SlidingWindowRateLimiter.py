import RateLimiterInterface, BlockingQueue, time

class SlidingWindow(RateLimiterInterface):
    def __init__(self, timeWindowInSeconds, bucketCapacity):
        self.timeWindowInSeconds = timeWindowInSeconds
        self.bucketCapacity = bucketCapacity
        self.slidingWindow = BlockingQueue.BlockingQueue()

    def grantAccess(self):
        currentTime = time.nowInMillis()
        self.checkAndUpdateQueue(currentTime)
        if self.slidingWindow.curr_size < self.bucketCapacity:
            self.slidingWindow.enqueue(currentTime)
            return True
        return False
    
    def checkAndUpdateQueue(self, currentTime):
        if self.slidingWindow.curr_size == 0:
            return
        calculatedTimeInSeconds = (currentTime - self.slidingWindow.peek()) / 1000
        while calculatedTimeInSeconds >= self.timeWindowInSeconds:
            self.slidingWindow.dequeue()
            if self.slidingWindow.curr_size == 0:
                break
            calculatedTimeInSeconds = (currentTime - self.slidingWindow.peek()) / 1000


class UserBucketCreator:
    def __init__(self, id) -> None:
        self.bucket = dict() # Map of int, SlidingWindow
        self.bucket[id] = SlidingWindow(1, 10)

    def accessApplication(self, id):
        if id in self.bucket and self.bucket[id].grantAccess():
            print ("able to access application")
        else:
            print("Too many request, please try after sometime")

import time
from collections import deque

class SlidingWindowRateLimiter:
    '''
    A sliding window rate limiter is a variant of rate limiting where the 
    window of time slides continuously rather than being fixed.

    window_size which defines the time window in seconds
    max_requests which specifies the maximum number of requests allowed within the window.

    allow_request method removes expired requests from the window by 
    continuously checking the timestamps stored in the deque and 
    popping requests that fall outside the current window.

    If the number of requests within the window is below the maximum limit, 
    the current request time is added to the window, and the method returns True 
    to indicate that the request is allowed. 
    Otherwise, it returns False to indicate that the request is rate-limited.

    This implementation enforces a sliding window rate limit where the window continuously moves forward in time, 
    allowing requests at a steady rate within the specified window size. 
    Adjusting the window_size and max_requests parameters allows you to control the 
    rate limiting behavior according to your requirements.
    '''
    def __init__(self, window_size, max_requests):
        self.window_size = window_size  # Time window in seconds
        self.max_requests = max_requests  # Maximum number of requests allowed in the window
        self.request_times = deque()  # Deque to store timestamps of requests

    def allow_request(self):
        current_time = time.time()

        # Remove expired requests from the window
        while self.request_times and self.request_times[0] < current_time - self.window_size:
            self.request_times.popleft()

        # Check if the number of requests within the window exceeds the limit
        if len(self.request_times) < self.max_requests:
            # Add the current request time to the window
            self.request_times.append(current_time)
            return True
        else:
            return False

# Example usage:
rate_limiter = SlidingWindowRateLimiter(window_size=10, max_requests=5)

for i in range(15):
    if rate_limiter.allow_request():
        print(f"Request {i + 1}: Allowed")
    else:
        print(f"Request {i + 1}: Rate limited")

    # Simulate some delay between requests
    time.sleep(1)
