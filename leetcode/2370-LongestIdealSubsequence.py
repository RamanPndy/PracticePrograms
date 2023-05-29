from collections import defaultdict

class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Input: s = "acfgbd", k = 2
        Output: 4
        Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
        Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
        """
        dp = defaultdict(int)
        for ch in s:
            newval = 0
            for prev in dp:
                if abs(ord(prev) - ord(ch)) <= k:
                    newval = max(newval, dp[prev])
            dp[ch] = newval + 1
        return max(dp.values())