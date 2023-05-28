from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        fd = defaultdict()
        for num in nums:
            fd[num] += 1
        sl = sorted(fd, key=lambda n: (-fd[n], n))
        return sl[:k]