class Solution:
    '''
    You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

    Question: What is the minimum number of minutes required for all fresh oranges to become rotten, or -1 if it is impossible?
    Intuition: The rotting process spreads from rotten oranges to adjacent fresh oranges in a breadth-first manner. 
    By simulating this process level by level, we can determine the minimum time required.
    Steps:
    1. Count the number of fresh oranges and initialize a queue with the positions of all rotten oranges.
    2. Perform a breadth-first search (BFS) from the rotten oranges, spreading the rot to adjacent fresh oranges.
    3. Keep track of the time elapsed during the BFS.
    4. If all fresh oranges become rotten, return the time; otherwise, return -1.
    Time Complexity: O(m * n), where m and n are the dimensions of the grid, as each cell is processed at most once.
    Space Complexity: O(m * n) for the queue in the worst case when all oranges are rotten initially.
    Interview Explanation: The key insight is to use a breadth-first search (BFS) to simulate the rotting process. 
    By processing the rotten oranges level by level, we can accurately track the time required for all fresh oranges to become rotten.
    '''
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