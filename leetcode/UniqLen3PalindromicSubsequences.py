class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        Then first and last index of that three letter word should be same for the palindromic condition.Between character can be all the unique charater present between that both index.
        1. find the index (from starting and ending both) of each unique character in the string.
        2. Then if starting index < ending index of that charactrer.
        3. Add the number of unique characters present between them.
        """
        res = 0
        uniq = set(s)
        for c in uniq:
            si = s.find(c)
            ei = s.rfind(c)
            if si < ei:
                res += len(set(s[si+1:ei]))
        return res