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

        Question: Can you find the number of unique paths for a robot to move from the top-left corner to the bottom-right corner of an m x n grid?
        Approach:
        - Use dynamic programming to build a 2D array `dp` where `dp[i][j]` represents the number of unique paths to reach cell `(i, j)`.
        - Initialize the first row and first column with 1 since there is only one way to reach those cells.
        - For each cell `(i, j)` not in the first row or first column, calculate `dp[i][j]` as the sum of `dp[i-1][j]` and `dp[i][j-1]`.
        - Return the value in the bottom-right cell `dp[m-1][n-1]` as the total number of unique paths.
        Time complexity: O(m * n), where m is the number of rows and n is the number of columns, as we iterate through the entire grid once.
        Space complexity: O(m * n), as we use a 2D array of the same size as the grid to store the intermediate results.
        Example:
        Input: m = 3, n = 7
        Output: 28
        Explanation: There are 28 unique paths for a robot to move from the top-left corner to the bottom-right corner of a 3x7 grid.
        The robot can only move either down or right at any point in time, so the number of unique paths is determined by the combinations of these moves.
        In this example, the robot has to make a total of 3-1 = 2 moves down and 7-1 = 6 moves right, and the number of unique paths is the number of ways to arrange these moves.
        The total number of unique paths can be calculated using the combination formula C(m+n-2, m-1) or C(m+n-2, n-1), which represents the number of ways to arrange the moves down and right.
        For the given example of a 3x7 grid, the total number of unique paths is C(3+7-2, 3-1) = C(8, 2) = 28.
        Note: The combination formula C(m+n-2, m-1) is derived from the fact that the robot needs to make a total of (m-1) moves down and (n-1) moves right, and we need to choose (m-1) positions for the down moves out of the total (m+n-2) moves.
        Another approach to solve this problem is to use combinatorics directly without building the DP table. The number of unique paths can be calculated using the combination formula C(m+n-2, m-1) or C(m+n-2, n-1).
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