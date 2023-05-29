class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l, r = 0, 0
        q = [(l, r, '')]
        res = []
        while q:
            l, r, s = q.pop()
            if len(s) == n * 2:
                res.append(s)
            if l < n:
                q.append((l +1, r, s + '('))
            if r < l:
                q.append((l, r + 1, s + ')'))
        return res