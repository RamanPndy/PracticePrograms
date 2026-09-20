'''
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''
class Solution:
    """
    Question: Can you generate all possible subsets of a given list of numbers?
    Approach:
    - Use a depth-first search (DFS) approach to explore all possible subsets.
    - Start from the first number and recursively build subsets by including or excluding the current number.
    - Backtrack by removing the last added number and try the next possibility.
    - Continue until all subsets are generated.
    Time complexity: O(2^n * n), where n is the length of nums, as we generate all possible subsets and each subset takes O(n) time to construct.
    Space complexity: O(n), as the recursion stack can go up to depth n.
    Steps:
    1. Define a helper function dfs(i) to perform depth-first search.
    2. If the index i reaches the length of nums, append a copy of the current subset to the result list and return.
    3. Include the current number in the subset and recursively call dfs with the next index.
    4. Exclude the current number from the subset and recursively call dfs with the next index.
    5. Initialize the result list and call dfs starting from index 0.
    6. Return the result list containing all subsets.
    Explanation: The DFS approach explores all possible subsets by recursively including or excluding each number. The result list accumulates all valid subsets.
    Example:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    Notes:
    - The order of numbers in each subset does not matter.
    - The subsets themselves are returned in lexicographical order based on the numbers.
    - The solution uses backtracking to efficiently explore all possible subsets without generating duplicates.
    - The solution ensures that all subsets are unique and no subset is repeated.
    - The solution can be adapted to generate subsets of any size and from any list of numbers.
    """
    def subsets(self, nums):
        res = []
        subsets = []
        def dfs(i):
            if i >= len(nums):
                res.append(subsets[:])
                return
            
            #if we include nums[i]
            subsets.append(nums[i])
            dfs(i+1)

            #if we don't include nums[i]
            subsets.pop()
            dfs(i+1)
        dfs(0)
        return res