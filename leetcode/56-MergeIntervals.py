class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
        Steps:
        1. sort all given intervals
        2. put first in result array
        3. iterate through all remaining intervals
            - get end of last interval from last entry of result array
            - if last interval end >= current interval start then update last interval end with maximum of current interval end and last interval end
            - else append current interval in result array
        4. return result
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