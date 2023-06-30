class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        1. The idea is to add ')' only after valid '('
        2. We use two integer variables left & right to see how many '(' & ')' are in the current string
        3. If left < n then we can add '(' to the current string
        4. If right < left then we can add ')' to the current string
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