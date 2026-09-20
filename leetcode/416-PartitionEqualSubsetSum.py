class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Input: nums = [1,5,11,5]
        Output: true
        Explanation: The array can be partitioned as [1, 5, 5] and [11]. 
        Steps:
        1. get the total sum of numbers
        2. if total sum is odd return false.
        3. target will be half of total sum
        4. create a dp list of length (target + 1) with values as false
        5. set first dp[0] = true
        6. traverse through numbers
            - traverse in reverse order from target to number
            - dp[i] = dp[i] or dp[i-n]
        7. return dp[target]
        Intuition: The problem can be solved using dynamic programming. We aim to find a subset of numbers that sums up to half of the total sum. 
        Strategy: Use a dynamic programming approach to determine if a subset with a sum equal to half of the total sum exists.
        If such a subset exists, the remaining numbers will also sum up to half of the total sum, thus partitioning the array into two equal subsets.
        Steps:
        1. Calculate the total sum of the array.
        2. If the total sum is odd, return False.
        3. Set the target sum as half of the total sum.
        4. Initialize a dp array of size (target + 1) with False values.
        5. Set dp[0] = True.
        6. Iterate through each number in the array and update the dp array.
        7. Return dp[target].
        Time Complexity: O(n * target), where n is the number of elements in the array and target is half of the total sum.
        Space Complexity: O(target), for the dp array.
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        # Calculate the target sum for each subset
        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            # Traverse the dp array in reverse order to avoid using the same number multiple times.
            for i in range(target, n-1, -1):
                # If we can form a sum j-num using the previous elements in the input array,
                # we can also form a sum j using the current element
                dp[i] = dp[i] or dp[i-n]
        return dp[target]