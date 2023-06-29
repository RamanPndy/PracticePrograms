class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Given an integer array nums, find the subarray with the largest sum, and return its sum.
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: The subarray [4,-1,2,1] has the largest sum 6.
        """
        # currSum = 0
        # maxSum = 0
        # for n in nums:
        #     currSum += n
        #     maxSum = max(maxSum, currSum)
        #     if currSum < 0:
        #         currSum = 0
        # return maxSum
        answer = float('-inf')
        maximum=0

        for num in nums:
            maximum += num
            answer = max(answer, maximum)
            maximum = max(maximum, 0)
        return answer 