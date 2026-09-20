class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        Intuition: The problem can be solved using a depth-first search (DFS) approach. 
        We start DFS from the cells adjacent to the Pacific and Atlantic oceans and mark all reachable cells. 
        The intersection of these reachable cells gives the result.
        Strategy: Use DFS to explore all cells reachable from the Pacific and Atlantic oceans separately, and 
        then find the intersection of these sets to get the final result.
        Steps:
        1. Initialize sets to keep track of cells reachable from the Pacific and Atlantic oceans.
        2. Perform DFS from the cells adjacent to the Pacific and Atlantic oceans.
        3. For each cell, check if it is reachable from both oceans and add it to the result list if it is.
        4. Return the result list.
        Time Complexity: O(M * N), where M is the number of rows and N is the number of columns, as each cell is visited at most twice.
        Space Complexity: O(M * N), for the recursion stack and the visited sets.
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
            # Perform DFS for the top and bottom rows (Pacific and Atlantic oceans)
            dfs(0, c, pac, heights[0][c])
            # Perform DFS for the bottom row (Atlantic ocean)
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            # Perform DFS for the left and right columns (Pacific and Atlantic oceans)
            dfs(r, 0, pac, heights[r][0])
            # Perform DFS for the right column (Atlantic ocean)
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

