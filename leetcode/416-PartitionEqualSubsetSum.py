class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Input: nums = [1,5,11,5]
        Output: true
        Explanation: The array can be partitioned as [1, 5, 5] and [11].
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        # Calculate the target sum for each subset
        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for i in range(target, n-1, -1):
                # If we can form a sum j-num using the previous elements in the input array,
                # we can also form a sum j using the current element
                dp[i] = dp[i] or dp[i-n]
        return dp[target]