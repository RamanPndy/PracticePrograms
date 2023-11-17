class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        Input: strs = ["flower","flow","flight"]
        Output: "fl"
        Steps:
        1. sort all strings
        2. get first and last string 
        3. get minimum length of first and last string
        4. set res string and traverse until range of min length calculated in step 3
            - if first[i] == last[i] then append first[i] to res 
            - else break the loop
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