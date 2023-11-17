class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        Steps:
        1. create res array with then same length as nums with prefilled value as 1
        2. create a neutral val as suffix
        3. traverse nums array by index from index 1 and update res at index i by muliplying prev val with prev num
        4. traverse nums array in reverse 
            - update res at index i by muliplying current index val with suffix
            - update suffix by muliplying current nums index val with suffix
        5. return res
        """
        res = [1] * len(nums)
        suffix = 1
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res