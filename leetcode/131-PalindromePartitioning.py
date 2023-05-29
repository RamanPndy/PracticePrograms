class Solution(object):
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        backtracking
        Input: s = "aab"
        Output: [["a","a","b"],["aa","b"]]
        """
        res  = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range (i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i: j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
        