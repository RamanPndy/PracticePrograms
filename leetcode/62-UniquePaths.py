class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        There is a robot on an m x n grid. The robot is initially located at the top-left corner 
        (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
        The robot can only move either down or right at any point in time.
        Given the two integers m and n, return the number of possible unique paths that the robot can take to 
        reach the bottom-right corner.
        Input: m = 3, n = 7
        Output: 28
        total combinations for reaching
        dp[i][j] = dp[i-1][j] (*from the left*) + dp[i][j-1] (*from the top*) for i != 0 and j != 0
        For initializing the dp matrix, we need to set 1 to the first row and first column because there is only 
        one way to reach dp[0][j] and dp[i][0]
        When we're at the position [1,1] then we could get there by first moving to [0, 1] or [1, 0] so that gives us 2 options 
        to get there so we need to sum them.
        Steps:
        1. build a 2D array to store the number of unique paths for each cell in the grid.
        2. initialize the first row and first column with a value of 1 since there is only one way to reach it.
        3. iterate through the grid row by row and calculate the number of unique paths for each cell by adding the number of 
            unique paths from the cell above it and the cell to the left of it. 
        4. value in the bottom-right cell represents the total number of unique paths.
        Time complexity:  O(m * n) since we iterate through the entire grid once to calculate the unique paths for each cell.
        Space complexity: O(m * n) since we use a 2D array of the same size as the grid to store the intermediate results.
        """
        dp = [[1 for i in range(n)] for j in range(m)]
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]