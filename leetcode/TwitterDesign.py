from collections import defaultdict
import heapq

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) #Map userId -> [(count, tweetId)]
        self.followMap = defaultdict(set) #Map userId -> [followeeId]
        
    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                lastIndex = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][lastIndex]
                minHeap.append([time, tweetId, followeeId, lastIndex - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            #check if followee has more tweets
            if index > 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        

class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i=len(self.tweets)-1
        while i>=0 and len(res)<10:
            if self.tweets[i][0] in self.users[userId] or self.tweets[i][0]==userId:
                res.append(self.tweets[i][1])
            i-=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)