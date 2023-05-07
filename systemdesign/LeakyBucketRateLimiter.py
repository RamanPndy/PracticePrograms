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
