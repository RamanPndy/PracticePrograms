class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
        Step 1: define the dp array
        dp[i] represents the length of the longest increasing subsequence that ends with nums[i].
        Step 2: find the dp rule
        Here is the rule:
        dp[i] = max(dp[i], dp[j]+1) for each j<i and dp[j]< dp[i].
        I keep trying to update the dp[i] with a longest candidate dp[j]. That will keep the solution optimal.
        Step 3: determine the initial state and the order
        For the initial value of dp array, I set them all to 1 
        (according to the description, the length is at least 1). 
        And I gonna iterate through the input array from the left to the right.
        """
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range (i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) + 1