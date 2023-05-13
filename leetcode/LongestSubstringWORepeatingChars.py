class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = dict()
        ans,l,r = 0,0,0
        while (r < len(s)):
            c = s[r]
            if c in m:
                m[c] = m[c] + 1
            else:
                m[c] = 1
            while (m[c] > 1):
                t = s[l]
                m[t] = m[t] - 1
                l = l + 1
            ans = max(ans, r-l+1)
            r = r + 1
        return ans