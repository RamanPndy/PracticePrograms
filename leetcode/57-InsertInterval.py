class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]
        """
        res = []
        for i, (start, end) in enumerate(intervals):
            #if new interval end is less than curent interval start then push new interval
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            #if new interval start is greater than current interval end then push current interval
            elif newInterval[0] > end:
                res.append([start, end])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        res.append(newInterval)
        return res