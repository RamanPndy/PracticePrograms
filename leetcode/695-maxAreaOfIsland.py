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
        Question: Find the maximum area of an island in the given grid.
        Intuition: Use depth-first search (DFS) to explore each island and calculate its area.
        Steps:
        1. get total rows and columns and create visited set which will hold visited row and column
        2. run dfs on grid
            for current row and column check base condition:
                - row should not be < 0 or = ROWS
                - col should not be < 0 or = COLS
                - should not be water
                - should not be in visited set
            check the area of the current island by recursively visiting all connected land cells and summing up their count.
        Time Complexity: O(R*C), where R is the number of rows and C is the number of columns, as we potentially visit each cell once.
        Space Complexity: O(R*C) for the visited set in the worst case when the entire grid is land.
        """
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            # Recursively visit all connected land cells (4-directionally) and sum up their count to calculate the area of the current island.
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r,c))
        return maxArea

    def areaOfIsland(self, grid):
        '''
        Find the maximum area of an island in the given grid using breadth-first search (BFS).
        Intuition: Use breadth-first search (BFS) to explore each island and calculate its area.
        Steps:
        1. get total rows and columns and create visited set which will hold visited row and column
        2. run bfs on grid
            for current row and column check base condition:
                - row should not be < 0 or = ROWS
                - col should not be < 0 or = COLS
                - should not be water
                - should not be in visited set
            check the area of the current island by iteratively visiting all connected land cells and summing up their count.
        Time Complexity: O(R*C), where R is the number of rows and C is the number of columns, as we potentially visit each cell once.
        Space Complexity: O(R*C) for the visited set and the queue in the worst case when the entire grid is land.
        '''
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = [(r, c)]
            visited.add((r, c))
            area = 0
            while queue:
                row, col = queue.pop(0)
                area += 1
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return area

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea