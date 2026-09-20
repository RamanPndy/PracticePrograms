class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        Question: Can you generate all possible combinations of k numbers out of the range 1 to n?
        Approach:
        - Use a depth-first search (DFS) approach to explore all possible combinations.
        - Start from the first number and recursively build combinations by adding the next number.
        - Backtrack by removing the last added number and try the next possibility.
        - Continue until all combinations of length k are generated.
        Time complexity: O(C(n, k) * k), where C(n, k) is the number of combinations, as we generate all combinations and each combination takes O(k) time to construct.
        Space complexity: O(k), as the recursion stack can go up to depth k.
        Steps:
        1. Define a helper function dfs(start, path) to perform depth-first search.
        2. If the length of the current path equals k, append a copy of the path to the result list and return.
        3. Iterate through numbers from start to n.
        4. Append the current number to the path and recursively call dfs with the next start value.
        5. Backtrack by removing the last added number from the path.
        6. Initialize the result list and call dfs starting from 1 with an empty path.
        7. Return the result list containing all combinations.
        Explanation: The DFS approach explores all possible combinations by recursively adding numbers to the current path and backtracking when necessary. The result list accumulates all valid combinations of length k.
        Example:
        Input: n = 4, k = 2
        Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        Explanation: The example demonstrates generating all combinations of 2 numbers out of the range 1 to 4.
        Notes:
        - The order of numbers in each combination does not matter.
        - The combinations themselves are returned in lexicographical order based on the numbers.
        - The solution uses backtracking to efficiently explore all possible combinations without generating duplicates.
        - The solution ensures that all combinations are unique and no combination is repeated.
        - The solution can be adapted to generate combinations of any size and from any range of numbers.
        """
        def dfs(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            else:
                for i in range(start, n+1):
                    path.append(i)
                    dfs(i+1, path)
                    path.pop()
                return res
                
        res = []
        dfs(1, [])
        return res
