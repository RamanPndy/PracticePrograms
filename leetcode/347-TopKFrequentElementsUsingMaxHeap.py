from collections import defaultdict
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        Steps:
        1. create frequency map of numbers
        2. traverse frequency map
            - push frequency and number in the heap
        3. create result array
        4. while k > 0
            - get value from heap and append in result array
            - decrease k
        5. return result
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