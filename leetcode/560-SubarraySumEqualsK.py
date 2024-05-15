from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
        Input: nums = [1,1,1], k = 2
        Output: 2
        Kadane algorithm
        the basic idea behind this is whenever sums has increased by a value of k, we've found a subarray of sums=k. (prefix sum)
        if you notice the running sums array, from 1->4, there is increase of k and from 4->7, 
        there is an increase of k. So, we've found 2 subarrays of sums=k.
        However, if sums==k, it should've been 3-0=k. But 0 is not present in the array. 
        To account for this case, we include the 0.
        Steps:
        1. create vars res and currSum
        2. create prefixSum map with intital value as 0 and count is 1.
        3. traverse through nums
            - add num in currSum
            - calculate difference between currSum and k
            - if diff exists in prefixSum that means it has been already calculated and prefixSum count can be added in result
            - update prefixSum for currSum by increasing value by 1 at currSum
        4. return res
        """
        res = 0
        currSum=0
        prefixSum = {0 : 1}
        for n in nums:
            currSum += n
            diff = currSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        return res
