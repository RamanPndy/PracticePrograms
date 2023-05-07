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