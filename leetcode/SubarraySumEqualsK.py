from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Kadane algorithm
        the basic idea behind this is whenever sums has increased by a value of k, we've found a subarray of sums=k. (prefix sum)
        if you notice the running sums array, from 1->4, there is increase of k and from 4->7, there is an increase of k. So, we've found 2 subarrays of sums=k.
        However, if sums==k, it should've been 3-0=k. But 0 is not present in the array. To account for this case, we include the 0.
        """
        sums = 0
        count = 0
        d = defaultdict(int)
        d[0] = 1
        for n in nums:
            sums += n
            count += d[sums - k]
            d[sums] += 1
        return count
