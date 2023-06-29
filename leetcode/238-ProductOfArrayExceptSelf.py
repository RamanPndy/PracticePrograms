class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        """
        res = [1] * len(nums)
        suffix = 1
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res