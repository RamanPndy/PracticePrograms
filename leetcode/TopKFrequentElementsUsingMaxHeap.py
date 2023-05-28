from collections import defaultdict
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        
        heap = []
        for k, v in m.items():
            #appending minus because we're using max heap and heapq doesn't support maxheap 
            heapq.heappush(heap, (-v, k))
        res = []
        while k > 0:
            val = heapq.heappop(heap)
            res.append(val[1])
            k -= 1
        return res