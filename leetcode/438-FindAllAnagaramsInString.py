from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        Input: s = "cbaebabacd", p = "abc"
        Output: [0,6]
        Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".
        """
        if len(p) > len(s):
            return []
        m = defaultdict(int)
        n = defaultdict(int)

        for i in range(len(p)):
            m[p[i]] += 1
            n[s[i]] += 1
        
        res = [0] if m == n else []
        l = 0
        for r in range(len(p), len(s)):
            n[s[r]] += 1
            n[s[l]] -= 1

            if n[s[l]] == 0:
                del n[s[l]]
            l += 1
            if m == n :
                res.append(l)
        return res
        