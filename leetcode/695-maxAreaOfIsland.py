class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Input: grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
        Output: 6
        Explanation: The answer is not 11, because the island must be connected 4-directionally.
        Steps:
        1. get total rows and columns and create visited set which will hold visited row and column
        2. run dfs on grid
            for current row and column check base condition:
                - row should not be < 0 or = ROWS
                - col should not be < 0 or = COLS
                - should not be water
                - should not be in visited set
            check 
        """
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r,c))
        return maxArea