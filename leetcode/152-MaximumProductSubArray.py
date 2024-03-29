class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.
        The intuition behind this approach is that a subarray with maximum product can be obtained by multiplying 
        the maximum product of its previous subarray with the current element 
        (if the current element is positive) or the minimum product of its previous subarray with the 
        current element (if the current element is negative). 
        We keep track of both the maximum and minimum products because a negative number can also 
        result in a maximum product if multiplied by another negative number.
        Steps:
        1. create 2 arrays maxProd and minProd of the same length as nums and fill 0 in it
        2. put num[0] in both maxProd and minProd at first index and assign same to result
        3. traverse remaining nums from index 1 by index
            - if current num is positive
                maxProd[i] = max(current num, previous value from maxProd * current num)
                minProd[i] = max(current num, previous value from minProd * current num)
            else
                maxProd[i] = max(current num, previous value from minProd * current num)
                minProd[i] = max(current num, previous value from maxProd * current num)
        4. update result with maxProd with current index
        """
        maxProd = [0 for i in range(len(nums))]
        minProd = [0 for i in range(len(nums))]
        maxProd[0] = minProd[0] = result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                maxProd[i] = max(nums[i], maxProd[i-1] * nums[i])
                minProd[i] = min(nums[i], minProd[i-1] * nums[i])
            else:
                maxProd[i] = max(nums[i], minProd[i-1] * nums[i])
                minProd[i] = min(nums[i], maxProd[i-1] * nums[i])
            result = max(result, maxProd[i])
        return result