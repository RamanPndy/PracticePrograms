class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        Input: s = "12"
        Output: 2
        Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
        """
        dp = {len(s) : 1}

        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if (i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                dp[i] += dp[i+2]
        return dp[0]