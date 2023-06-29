class Solution:
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0 , 0
        q = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.pop(0)
                for dr, dc in directions:
                    row,col = dr + r, dc + c
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((row,col))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1