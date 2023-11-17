class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        Input: grid = [[5,3],[4,0],[2,1]], moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
        Output: 17
        Explanation: The path with the minimum possible cost is the path 5 -> 0 -> 1.
        - The sum of the values of cells visited is 5 + 0 + 1 = 6.
        - The cost of moving from 5 to 0 is 3.
        - The cost of moving from 0 to 1 is 8.
        So the total cost of the path is 6 + 3 + 8 = 17.
        """
        rows, cols = len(grid), len(grid[0])
        dp = [[100000 for i in range(cols)] for i in range(rows)]
        num = 0
        for i in range(cols):
            dp[rows-1][i] = grid[rows-1][i]
        for i in range(rows - 2, -1, -1):
            for j in range(cols):
                num = grid[i][j]
                for k in range(cols):
                    dp[i][j] = min(dp[i][j], dp[i+1][k] + num + moveCost[num][k])
        return min(dp[0])