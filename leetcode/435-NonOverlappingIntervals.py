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
        Question: Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
        Intuition: To minimize the number of intervals to remove, always keep the interval with the earliest end time and remove overlapping intervals.
        Steps:
        1. Sort the intervals based on their start times.
        2. Initialize a variable to keep track of the end of the previous interval.
        3. Initialize a result variable to count the number of intervals to remove.
        4. Traverse through the rest of the intervals and apply the logic described above.
        5. Return the result.
        Time Complexity: O(n log n), where n is the number of intervals, due to sorting.
        Space Complexity: O(1), as we are using a constant amount of extra space.
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