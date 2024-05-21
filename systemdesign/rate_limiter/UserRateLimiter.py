import time

class UserRateLimiter:
    '''
    A user rate limiter restricts the number of requests 
    made by a specific user within a given time window.

    window_size, which defines the time window in seconds, 
    max_requests, which specifies the maximum number of 
    requests allowed for each user within the window.

    allow_request method takes a user_id as input and checks 
    if the user has made requests before. 
    If the user has made requests, it checks if the time window 
    has elapsed since the last request. If the window has elapsed, 
    it resets the request count for the user. 
    If not, it checks if the request count for the user is below the maximum limit. 
    If it is, it increments the count. If not, it denies the request.

    If the user has not made requests before, the method adds the user to the dictionary 
    with an initial request count and last request time.

    This implementation allows you to restrict the rate of requests on a per-user basis 
    within a specified time window. 
    Adjusting the window_size and max_requests parameters allows you to control 
    the rate limiting behavior according to your requirements.
    '''
    def __init__(self, window_size, max_requests):
        self.window_size = window_size  # Time window in seconds
        self.max_requests = max_requests  # Maximum number of requests allowed in the window
        self.user_requests = {}  # Dictionary to store user request counts and last request time

    def allow_request(self, user_id):
        current_time = time.time()

        # Check if the user has made requests before
        if user_id in self.user_requests:
            user_info = self.user_requests[user_id]
            # Check if the time window has elapsed since the last request
            if current_time - user_info[1] >= self.window_size:
                # Reset request count and update last request time
                user_info[0] = 1
                user_info[1] = current_time
                return True
            else:
                # Check if the request count exceeds the limit
                if user_info[0] < self.max_requests:
                    user_info[0] += 1
                    user_info[1] = current_time
                    return True
                else:
                    return False
        else:
            # Add user to the dictionary with initial request count and last request time
            self.user_requests[user_id] = [1, current_time]
            return True

# Example usage:
rate_limiter = UserRateLimiter(window_size=10, max_requests=5)

user_ids = ['user1', 'user2', 'user1', 'user2', 'user1', 'user1', 'user3', 'user2', 'user1', 'user2']

for i, user_id in enumerate(user_ids):
    if rate_limiter.allow_request(user_id):
        print(f"Request {i + 1} by {user_id}: Allowed")
    else:
        print(f"Request {i + 1} by {user_id}: Rate limited")

    # Simulate some delay between requests
    time.sleep(1)
