class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Traverse the given matrix, and for each unvisited cell that is part of an island, perform BFS starting from 
        that cell.
        In the BFS algorithm, enqueue the current cell and mark it as visited. 
        Then, while the queue is not empty, dequeue a cell and enqueue its unvisited neighbors that are part of the 
        same island. 
        Mark each of these neighbors as visited. After BFS is complete, increment the island count by 1.
        Repeat previous steps until all unvisited cells have been processed. Return the total island count.

        Question: Can you determine the number of islands in the given grid?
        Approach:
        - Use BFS to traverse each island starting from an unvisited land cell.
        - Maintain a visited set to keep track of visited cells.
        - For each unvisited land cell, perform BFS to mark all connected land cells as visited and increment the island count.
        Time Complexity: O(rows * cols), where rows and cols are the dimensions of the grid.
        Space Complexity: O(rows * cols), as we use a queue and a visited set to store the cells.
        Steps:
        1. Initialize a visited set and a counter for the number of islands.
        2. Define a BFS function that takes a starting cell, enqueues it, and marks it as visited.
        3. While the queue is not empty, dequeue a cell and enqueue its unvisited land neighbors, marking them as visited.
        4. Traverse each cell in the grid. If it is an unvisited land cell, perform BFS from that cell and increment the island counter.
        5. Return the island counter after processing all cells.
        Example:
        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3
        Explanation: There are three islands in the grid. The first island is formed by the top-left 2x2 block of "1"s, the second island is the single "1" in the middle, and the third island is the bottom-right 2x2 block of "1"s.
        Approach Summary:
        - Traverse the grid cell by cell.
        - When an unvisited land cell is found, perform BFS to mark all connected land cells as visited.
        - Increment the island count for each BFS initiated.
        - Continue until all cells have been processed.
        - Return the total number of islands found in the grid.
        Example Summary:
        - The input grid contains three distinct islands.
        - The BFS traversal ensures that all connected land cells are visited for each island.
        - The counter accurately reflects the total number of islands after processing the entire grid.
        Key Points:
        - BFS is used to explore all connected land cells starting from an unvisited land cell.
        - The visited set ensures that each cell is processed only once.
        - The counter is incremented only when a new island is discovered.
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