import time

class FixedWindowRateLimiter:
    '''
    window_size which defines the time window in seconds 
    max_requests which specifies the maximum number of requests allowed within the window.

    allow_request method checks if the current time falls within the window and 
    if the number of requests made within the window is below the maximum limit. 
    If both conditions are met, the request is allowed, and 
    the current request time is added to the list of request times. 
    Otherwise, the request is rate-limited.

    Requests outside the current window are removed from the request_times list to 
    keep track of only the requests within the window.

    This implementation enforces a strict limit on the number of requests allowed within a fixed time window. 
    Adjusting the window_size and max_requests parameters allows you to control the rate limiting behavior 
    according to your requirements.
    '''
    def __init__(self, window_size, max_requests):
        self.window_size = window_size  # Time window in seconds
        self.max_requests = max_requests  # Maximum number of requests allowed in the window
        self.request_times = []  # List to store timestamps of requests

    def allow_request(self):
        current_time = time.time()

        # Remove requests that fall outside the current window
        self.request_times = [t for t in self.request_times if t > current_time - self.window_size]

        # Check if the number of requests within the window exceeds the limit
        if len(self.request_times) < self.max_requests:
            # Add the current request time to the list
            self.request_times.append(current_time)
            return True
        else:
            return False

# Example usage:
rate_limiter = FixedWindowRateLimiter(window_size=10, max_requests=5)

for i in range(10):
    if rate_limiter.allow_request():
        print(f"Request {i + 1}: Allowed")
    else:
        print(f"Request {i + 1}: Rate limited")

    # Simulate some delay between requests
    time.sleep(1)
