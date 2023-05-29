class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
        """
        intervals = sorted(intervals)
        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if lastEnd >= start:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
        return res