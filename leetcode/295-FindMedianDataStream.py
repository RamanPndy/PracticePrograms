class MedianFinder(object):

    def __init__(self):
        self.data = []
        self.length = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        Question: Where should the new number be inserted in the sorted data stream to maintain order?
        Approach:
        - Use binary search to find the correct insertion position for the new number.
        Time Complexity: O(log n) for finding the insertion position, O(n) for inserting into the list.
        Space Complexity: O(1) as we are using only a constant amount of extra space.
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
        Question: How can we find the median of the current data stream efficiently?
        Approach:
        - If the length of the data is even, the median is the average of the two middle elements.
        - If the length of the data is odd, the median is the middle element.
        Time Complexity: O(1) as we are directly accessing the middle elements.
        Space Complexity: O(1) as we are using only a constant amount of extra space.
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