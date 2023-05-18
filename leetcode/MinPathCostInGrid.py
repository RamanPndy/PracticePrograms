class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        dp = [[100000 for i in range(cols)] for i in range(rows)]
        num = 0
        for i in range(cols):
            dp[rows-1][i] = grid[rows-1][i]
        for i in range(rows - 2, -1, -1):
            for j in range(cols):
                num = grid[i][j]
                for k in range(cols):
                    dp[i][j] = min(dp[i][j], dp[i+1][k] + num + moveCost[num][k])
        return min(dp[0])