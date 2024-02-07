import time

class FixedWindowCounter:
    '''
    A fixed window counter algorithm counts the number of requests within 
    a fixed time window and resets the count after the window expires.

    window_size, which specifies the time window in seconds.

    allow_request method checks if the current time exceeds 
    the start time of the window plus the window size. 
    If it does, it resets the request count to 1 and 
    updates the window start time to the current time, allowing the request. 
    Otherwise, it increments the request count and 
    allows the request if the count is within a certain limit.

    request_count attribute tracks the number of requests made within the current window, 
    and the window_start_time attribute tracks the start time of the current window.

    This implementation enforces a fixed window counter algorithm, 
    allowing a specified number of requests within a fixed time window and 
    resetting the count after the window expires. 
    Adjusting the window_size parameter allows you to control the size of the time window 
    according to your requirements.
    '''
    def __init__(self, window_size):
        self.window_size = window_size  # Time window in seconds
        self.request_count = 0  # Count of requests made within the window
        self.window_start_time = time.time()  # Start time of the current window

    def allow_request(self):
        current_time = time.time()

        # Check if the current time exceeds the window start time plus window size
        if current_time >= self.window_start_time + self.window_size:
            # Reset the counter and update the window start time
            self.request_count = 1
            self.window_start_time = current_time
            return True
        else:
            # Increment the request count if still within the window
            self.request_count += 1
            return self.request_count <= self.max_requests

# Example usage:
window_counter = FixedWindowCounter(window_size=10)

for i in range(15):
    if window_counter.allow_request():
        print(f"Request {i + 1}: Allowed")
    else:
        print(f"Request {i + 1}: Rate limited")

    # Simulate some delay between requests
    time.sleep(1)
