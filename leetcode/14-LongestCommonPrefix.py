class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        f,l = strs[0], strs[len(strs)-1]
        N = min(len(f),len(l))
        res = ""
        for i in range(N):
            if f[i] == l[i]:
                res = res + f[i]
            else:
                break
        return res