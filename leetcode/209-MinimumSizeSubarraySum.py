class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        Input: target = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: The subarray [4,3] has the minimal length under the problem constraint.
        2 pointer approach.

        Question: Can you find the minimal length of a contiguous subarray of which the sum is at least target?
        Approach:
        - Use a sliding window with two pointers to find the minimal length subarray.
        - Expand the right pointer to increase the window sum.
        - Shrink the left pointer to decrease the window sum while maintaining the sum >= target.
        - Keep track of the minimal length encountered.
        Time Complexity: O(n) where n is the length of the input array nums.
        Space Complexity: O(1) as we are using a constant amount of extra space.
        Steps:
        1. create left,right pointer and set solutions as 0 initially.
        2. start from right pointer and add value in solution.
        3. if solution becomes greater than target then subtract left point value from solution and increment left pointer also 
            update res which will be legth of left and right pointer window.
        4. if res > len(nums) return 0 otherwise return res
        """
        res = len(nums) + 1
        l = s = 0
        for r, v in enumerate(nums):
            s += v
            while s >= target:
                s -= nums[l]
                res = min(res, r - l + 1)
                l += 1
        return 0 if res > len(nums) else res