class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        Question: Find the area of the largest square containing only 1's in the given binary matrix.
        Approach: Use dynamic programming to keep track of the size of the largest square ending at each cell.
        The value at dp[i][j] represents the side length of the largest square whose bottom-right corner is at cell (i, j).
        The side length of the largest square can be found by taking the maximum value in the dp table.

        Why this works: For each cell containing '1', we check the minimum of the largest squares ending at the top, 
        left, and top-left neighbors. 
        This ensures that we can form a square with the current cell as the bottom-right corner only if all three 
        neighbors can form squares of appropriate sizes.
        
        Time Complexity: O(m * n) where m and n are the dimensions of the matrix.
        Space Complexity: O(m * n) for the dp table.
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side