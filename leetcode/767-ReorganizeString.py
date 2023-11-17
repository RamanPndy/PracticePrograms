import heapq
from collections import defaultdict

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        Input: s = "aab"
        Output: "aba"
        Steps:
        1. create character frequency map
        2. create max heap and push (frequency and character) in heap
        3. traverse heap
            - get frquency and character from heap
            - reduce frequency of character in frequency map and append character in res string
            - if there is any cached character then get cached character frequency and push it to heap
            - if frequency is negative then put current character in cached character
        4. return empty string if cached character is not empty and it's frequency is positive otherwise return res.
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