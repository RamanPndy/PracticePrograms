from collections import defaultdict

class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dp = defaultdict(int)
        for ch in s:
            newval = 0
            for prev in dp:
                if abs(ord(prev) - ord(ch)) <= k:
                    newval = max(newval, dp[prev])
            dp[ch] = newval + 1
        return max(dp.values())