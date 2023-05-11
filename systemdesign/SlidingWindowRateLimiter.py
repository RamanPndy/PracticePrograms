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