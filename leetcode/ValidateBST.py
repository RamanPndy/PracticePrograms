# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        s, p = [], float('-INF')
        while s or root:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            if root.val <= p:
                return False
            p = root.val
            root = root.right
        return True