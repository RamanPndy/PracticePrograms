from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        1.Traverse the string from left to right, with the right end of the window (r) expanding as long as 
        there are no repeating characters.
        2.When a repeating character is found at index r, we update the left end of the window (l) to the 
        next index of the repeated character.
        3.Update the map with the current index of the repeated character.
        4.Update ans with the maximum length of the current substring and the previous maximum.
        """
        m = defaultdict(int)
        ans,l,r = 0,0,0
        while (r < len(s)):
            c = s[r]
            m[c] += 1
            while (m[c] > 1):
                t = s[l]
                m[t] -= 1
                l = l + 1
            ans = max(ans, r-l+1)
            r = r + 1
        return ans