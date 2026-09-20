class Solution(object):
    def jump(self, nums):
        """
        You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

        Each element nums[i] represents the maximum length of a forward jump from index i. 
        In other words, if you are at index i, you can jump to any index (i + j) where:

        0 <= j <= nums[i] and
        i + j < n
        Return the minimum number of jumps to reach index n - 1.


        Input: nums = [2,3,1,1,4]
        Output: 2
        Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, 
        then 3 steps to the last index.
        Return the minimum number of jumps to reach nums[n - 1]

        Question: Can you solve this problem in O(n) time complexity and O(1) space complexity?
        Approach:
        - Use a greedy approach to keep track of the farthest reachable index within the current number of jumps.
        - Increment the jump count whenever the current index exceeds the end of the current jump range.
        - Update the end of the current jump range to the farthest reachable index.
        - Continue this process until reaching the last index.
        Example:
        - Input: nums = [2,3,1,1,4]
        - Output: 2
        - Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, 
          then 3 steps to the last index.
          
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