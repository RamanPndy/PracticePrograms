class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [2,3,1,1,4]
        Output: 2
        Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, 
        then 3 steps to the last index.
        Return the minimum number of jumps to reach nums[n - 1]
        Time complexity: O(n)
        Space complexity: O(1)
        Steps:
        1. create vars for current and next end respectively
        2. set steps count to 0
        3. traverse through numbers by index
            - if current index is > current end:
                - increase step count
                - set current end to next end
            - update next end by max of next end and current index + nums[current index]
        4. return steps
        """
        cur_end, nxt_end = 0, 0
        steps = 0
        for i, n in enumerate(nums):
            if i > cur_end:
                steps += 1
                cur_end = nxt_end
            nxt_end = max(nxt_end, i + n)
        return steps