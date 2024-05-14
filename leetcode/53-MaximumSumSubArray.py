class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Given an integer array nums, find the subarray with the largest sum, and return its sum.
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: The subarray [4,-1,2,1] has the largest sum 6.
        Steps:
        1. create answer variable and assing positive infinity as max value
        2. create variable maximum and set it to 0.
        3. travers numbers
            - add number to maximum
            - update answer by max of answer and maximum value so far
            - update maximum by max of maximum and 0
        4. return answer
        """
        answer = float('-inf')
        maximum=0

        for num in nums:
            maximum += num
            answer = max(answer, maximum)
            maximum = max(maximum, 0)
        return answer 