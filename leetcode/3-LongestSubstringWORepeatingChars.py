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
        Steps:
        1. if string is empty then return 0
        2. create 2 vars res and maxLen which will hold result string and it's length.
        3. traverse through string character by character 
            - if current character is not present in res then add it and update maxLen with len(res)
            - else split res on current character and append 1st splitted character along with current character in res.

        # Time: O(n)
        # Space: O(1)  
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