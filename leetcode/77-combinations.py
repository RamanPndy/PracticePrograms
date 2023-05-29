class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            else:
                for i in range(start, n+1):
                    path.append(i)
                    dfs(i+1, path)
                    path.pop()
                return res
                
        res = []
        dfs(1, [])
        return res
