class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return
        rows, cols = len(grid), len(grid[0])
        visited = set()
        counter = 0
        def bfs(row, col):
            q = [(row, col)]
            visited.add((row, col))
            while q:
                r, c = q.pop(0)
                directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
                for dr,dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and 
                        col in range(cols) and 
                        grid[row][col] == "1" and 
                        (row, col) not in visited):
                        visited.add((row, col))
                        q.append((row, col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    counter += 1
        return counter