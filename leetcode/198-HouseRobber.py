class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        adjacent houses have security systems connected and it will automatically contact the police 
        if two adjacent houses were broken into on the same night.
        Input: nums = [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.

        Question: Can you determine the maximum amount of money you can rob without alerting the police?
        Approach:
        - Use dynamic programming to keep track of the maximum amount of money that can be robbed up to each house.
        - For each house, decide whether to rob it or skip it based on the maximum amount obtained from previous houses.
        Time Complexity: O(n), where n is the number of houses.
        Space Complexity: O(n), as we use an array to store the maximum amounts for each house.
        Steps:
        1. Handle the base cases where the list of houses is empty or contains only one house.
        2. Initialize a DP array to store the maximum amount that can be robbed up to each house.
        3. Set the first two values of the DP array based on the first two houses.
        4. Iterate through the remaining houses, updating the DP array with the maximum amount that can be robbed by either robbing the current house or skipping it.
        5. Return the last value of the DP array, which represents the maximum amount that can be robbed from all houses.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]