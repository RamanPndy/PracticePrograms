class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
        A good subarray is a subarray where:
        - its length is at least two, and
        - the sum of the elements of the subarray is a multiple of k.
        Input: nums = [23,2,4,6,7], k = 6
        Output: true
        Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

        Steps:
        1. create a remainder map which would be prefix map with initial value as 0 and index as -1
        2. create total variable
        3. traverse through nums by index and num:
            - calculate total by summing current num
            - calculate remainder by total % k
            - if remainder is not in remainder map then add remainder with it's current index
            - else if remainder is present in remainder map then current index - remainder index in map > 1 because 
                condition is subarray should be of size 2 then return True
        4. if no subarray found return false
        """
        # map remainder to end index
        remainder = {0 : -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False