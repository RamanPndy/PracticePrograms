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
        The idea is to update node values with the biggest, positive cumulative sum gathered by its children:
        If both contributions are negative, no value is added.
        If both are positive, only the biggest one is added, so that we don't include both children during the rest of the tree exploration.
        Leaves return its own value and we recursively work our way upwards.
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