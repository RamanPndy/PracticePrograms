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