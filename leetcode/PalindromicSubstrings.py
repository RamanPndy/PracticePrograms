class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        Manacher’s algorithm:
        """
        def expandAndCountPallindromes(i, j, s):
            '''
            Counts the number of pallindrome substrings from a given center i,j        
            1. when i=j, it's an odd-lengthed pallindrome string. 
                eg: for string "aba", i=j=1.
            2. when i+1=j, it's an even-lengthed pallindrome string. 
                eg: for string "abba", i=1, j=2.
            '''
            l = len(s)
            cnt = 0
            while i >=0 and j < l and s[i] == s[j]:
                i -= 1
                j += 1
                cnt += 1
            return cnt
        
        res = 0
        for i in range(len(s)):
            res += expandAndCountPallindromes(i, i, s) + expandAndCountPallindromes(i, i+1, s)
        return res