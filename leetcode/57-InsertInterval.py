class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]

        Question: Can you insert a new interval into the list of non-overlapping intervals and merge if necessary?
        Approach:
        - Initialize an empty result array.
        - Iterate through each interval in the list.
        - If the new interval ends before the current interval starts, append the new interval and the rest of the intervals to the result and return.
        - If the new interval starts after the current interval ends, append the current interval to the result.
        - Otherwise, merge the new interval with the current interval by updating the start to the minimum of both starts and the end to the maximum of both ends.
        - After the loop, append the new interval to the result.
        - Return the result array.

        Time complexity: O(n), where n is the number of intervals, as we iterate through the list once.
        Space complexity: O(n), as we are using a result array to store the merged intervals.
        Steps:
        1. create result array
        2. iterate through each interval by index
        3. if new interval end < curent interval start then push new interval and return with appending rest of intervals 
           from the current index
        4. if new interval start > current interval end then push current interval in result array
        5. otherwise update new interval with min of new interval start and current interval start and max of new interval end 
           and current interval end
        6. append new inteval in result array
        7. return result
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