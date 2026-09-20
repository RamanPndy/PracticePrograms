# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Input: root = [-10,9,20,null,null,15,7]
        Output: 42
        Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
        The idea is to update node values with the biggest, positive cumulative sum gathered by its children:
        If both contributions are negative, no value is added.
        If both are positive, only the biggest one is added, so that we don't include both children during the rest of the tree exploration.
        Leaves return its own value and we recursively work our way upwards.

        Question: Can you find the maximum path sum in a binary tree?
        Approach:
        - Use a depth-first search (DFS) to explore all paths in the binary tree.
        - At each node, calculate the maximum path sum including the node and its left and right children.
        - Update the global maximum path sum if the current path sum is greater.
        - Return the maximum path sum that can be extended to the parent node.
        Time Complexity: O(n), where n is the number of nodes in the binary tree.
        Space Complexity: O(h), where h is the height of the binary tree due to the recursion stack.
        Steps:
        1. Initialize a variable to store the global maximum path sum.
        2. Define a recursive DFS function to calculate the maximum path sum for each node.
        3. In the DFS function, return 0 if the node is None.
        4. Recursively calculate the maximum path sum for the left and right children, considering only positive contributions.
        5. Update the global maximum path sum with the sum of the current node value and the maximum contributions from both children.
        6. Return the maximum path sum that can be extended to the parent node.
        7. Call the DFS function with the root node.
        8. Return the global maximum path sum.
        """
        self.max_sum = float('-inf')
        def dfs(root):
            if not root:
                return
            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))

            # check if cumulative sum at current node > global max sum so far
            # this evaluates a candidate path
            self.max_sum = max(self.max_sum, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        dfs(root)
        return self.max_sum