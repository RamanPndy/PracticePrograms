class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
        Output: 7
        Question: Can you find the minimum path sum from the top-left corner to the bottom-right corner of a grid, where you can only move down or right?
        Approach:
        - Use dynamic programming to build a 1D array `dp` where `dp[j]` represents the minimum path sum to reach cell `(i, j)` in the current row.
        - Initialize the first element of `dp` with the first element of the grid.
        - Update the first row of `dp` by adding the corresponding grid elements.
        - For each subsequent row, update the first column of `dp` and then update the remaining columns by taking the minimum of the value from the left and the value from the top plus the current grid element.
        - Return the last element of `dp` as the minimum path sum from the top-left to the bottom-right corner.

        Time complexity: O(m * n), where m is the number of rows and n is the number of columns, as we iterate through the entire grid once.
        Space complexity: O(n), as we use a 1D array of size equal to the number of columns to store the intermediate results.

        Example:
        Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
        Output: 7
        Path: 1 → 3 → 1 → 1 → 1

        Steps:
        1. Initialize the dp array with the first row of the grid.
        2. Update the dp array for each subsequent row by taking the minimum path sum from the top or left.
        3. The last element of the dp array will contain the minimum path sum from the top-left to the bottom-right corner.
        
        Note: The approach uses a 1D array to optimize space complexity compared to using a 2D DP array.
        Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
        1. Initialize rows and cols as the number of rows and columns of the grid.
        2. Initialize dp list of size cols with the first element of dp being the first element of the first row of the grid.
        3. Loop through the remaining columns of the first row, updating each dp[i] as dp[i-1] + grid[0][i].
        4. Loop through the remaining rows of the grid, updating the first column of each row as dp[0] + grid[i][0].
        5. Loop through the remaining columns of the current row, updating each dp[j] as the 
            minimum of dp[j-1] and dp[j] plus the current grid element.
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