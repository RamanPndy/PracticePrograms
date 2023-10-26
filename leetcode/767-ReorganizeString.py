import heapq
from collections import defaultdict

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        Input: s = "aab"
        Output: "aba"
        """
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        heap = []
        for k, v in m.items():
            heapq.heappush(heap, (-v, k))
        res = ""
        cached_character = ''
        while heap:
            freq, c = heapq.heappop(heap)
            m[c] -= 1
            res += c
            if cached_character != '':
                cached_character_freq = m[cached_character]
                if cached_character_freq > 0:
                    heapq.heappush(heap, (-cached_character_freq, cached_character))
            if freq < 0:
                cached_character = c
            else:
                cached_character = ''
        return '' if cached_character != '' and m[cached_character] > 0 else res