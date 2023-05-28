class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [2,3,2]
        Output: 3
        Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
        ## LOGIC ##
        ## 1. Only 2 scenarios possible 
        ##     a) Rob 1st and donot rob last 
        ##     b) Rob last and donot rob first. 
        ## We take maximum of both cases.
        """
        def rob(nums):
            dp = [0 for i in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return max(dp[-1], dp[-2])
        if len(nums) <= 2:
            return max(nums)
        return max(rob(nums[1:]), rob(nums[:-1]))