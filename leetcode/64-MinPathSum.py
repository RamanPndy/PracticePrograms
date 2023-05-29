class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        dp = [1] * cols
        dp[0] = grid[0][0]
        for i in range(1, cols):
            dp[i] = dp[i-1] + grid[0][i]
        for i in range(1, rows):
            dp[0] += grid[i][0]
            for j in range(1, cols):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[cols-1]