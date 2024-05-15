class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
        Output: 1
        Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
        Steps:
        1. sort intervals
        2. get the end of first interval
        3. create result
        3. traverse through rest of intervals:
            - if start of current interval is > end of first interval then 
                update end of first interval with end of current interval
            - otherwise increase result and update end of first interval with 
                minimum of current interval end and first interval end
        4. return result
        """
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res