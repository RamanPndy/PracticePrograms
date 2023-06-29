class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        Input: s = "12"
        Output: 2
        Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
        this is a fibonacci dp question and a bottom up dp question
        Loop through s (i)
        if s[i] is a valid number (not 0) then we can include the previous permutation (s[i+1] permutation)
        if s[i] can be expressed as 10-26 then we include previous previous permutation (s[i+2] permutation)
        Note: it is s[i+1] because we are going reverse
        return the last permutation
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
    
        # left, right = 1, 0
        
        # for i in range(len(s)-1, -1, -1):
        #     ans = 0
        #     if s[i] != '0':
        #         ans += left
        #     if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
        #         ans += right
        #     left, right = ans, left
        # return left