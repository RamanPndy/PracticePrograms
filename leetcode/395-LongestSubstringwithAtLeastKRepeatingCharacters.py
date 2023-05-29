from collections import defaultdict
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Input: s = "aaabb", k = 3
        Output: 3
        Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
        """
        if len(s) < k:
            return 0

        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        for i, c in enumerate(s):
            if freq[c] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)
        
        return len(s)