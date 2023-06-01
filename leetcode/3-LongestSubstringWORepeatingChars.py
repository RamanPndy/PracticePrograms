class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        s = "abcbxy"
        s2 = "abbxy"
        s3 = "abcba"
        s4 = "aaaa"
        s5 = "abcd"
        s6 = "abcdaxyz"
        """
        res = ''
        maxLen = 1
        if not s:
            return 0
        for c in s:
            if c not in res:
                res += c
                maxLen = max(maxLen, len(res))
            else:
                res = res.split(c)[1] + c
        # print (res)
        return maxLen