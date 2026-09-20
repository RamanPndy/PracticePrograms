class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [2,3,2]
        Output: 3
        All houses at this place are arranged in a circle
        it will automatically contact the police if two adjacent houses were broken into on the same night.
        Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
        ## LOGIC ##
        ## 1. Only 2 scenarios possible 
        ##     a) Rob 1st and donot rob last 
        ##     b) Rob last and donot rob first. 
        ## We take maximum of both cases.

        Question: Given a list of non-negative integers representing the amount of money of each house arranged in a circle, determine the maximum amount of money you can rob without alerting the police.
        Approach:
        - Since the houses are arranged in a circle, the first and last houses are adjacent.
        - We have two scenarios to consider:
          1. Rob the first house and do not rob the last house.
          2. Rob the last house and do not rob the first house.
        - Use a helper function to calculate the maximum amount for a linear arrangement of houses.
        - Return the maximum value obtained from the two scenarios.
        Time Complexity: O(n) where n is the number of houses.
        Space Complexity: O(n) due to the dynamic programming array.
        Steps:
        1. Define a helper function robHouse to calculate the maximum amount for a linear arrangement of houses.
        2. Handle the base case where the number of houses is less than or equal to 2.
        3. Use the helper function to calculate the maximum amount for the two scenarios:
           a) Rob the first house and do not rob the last house.
           b) Rob the last house and do not rob the first house.
        4. Return the maximum value obtained from the two scenarios.
        """
        def robHouse(nums):
            dp = [0 for i in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return max(dp[-1], dp[-2])
        if len(nums) <= 2:
            return max(nums)
        return max(robHouse(nums[1:]), robHouse(nums[:-1]))