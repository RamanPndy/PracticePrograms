class MedianFinder(object):

    def __init__(self):
        self.data = []
        self.length = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        Steps:
        1. create left and right pointer with value 0 and length -1
        2. traverse while left <= right
            - get the mid index
            - if data at mid index is < input number then increase mid index by 1 and assign to left
            - otherwise decrease mid index by 1 an assign to right
        3. increase length by 1
        """
        l, r = 0, self.length -1
        while l <= r:
            m = (l + r)//2
            if self.data[m] < num:
                l = m + 1
            else:
                r = m - 1
        self.data.insert(l, num)
        self.length += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.length %2 == 0:
            t = self.length // 2
            return (self.data[t] + self.data[t-1])/2.0
        else:
            return self.data[self.length//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()