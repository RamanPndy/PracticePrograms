class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
        Output: 7
        Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
        1. Initialize rows and cols as the number of rows and columns of the grid.
        2. Initialize dp list of size cols with the first element of dp being the first element of the first row of the grid.
        3. Loop through the remaining columns of the first row, updating each dp[i] as dp[i-1] + grid[0][i].
        4. Loop through the remaining rows of the grid, updating the first column of each row as dp[0] + grid[i][0].
        5. Loop through the remaining columns of the current row, updating each dp[j] as the minimum of dp[j-1] and dp[j] plus the current grid element.
        6. Return the last element of dp which is the minimum path sum from top left to bottom right.

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