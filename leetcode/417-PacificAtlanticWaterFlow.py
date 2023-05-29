class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(heights), len(heights[0])
        pac , atl = set(), set()
        directions = [(0,1), (0, -1), (1,0), (-1,0)]
        res = []
        def dfs(r, c, visited, prevHeight):
            if (r,c) in visited or ROWS == r or r < 0 or COLS == c or c < 0 or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            for dx,dy in directions:
                dfs(r+dx, c+dy, visited, prevHeight)
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

