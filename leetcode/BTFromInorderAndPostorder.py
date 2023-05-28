# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        root_index_in_inorder = inorder.index(root.val)

        root.right = self.buildTree(inorder[root_index_in_inorder + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index_in_inorder], postorder)

        return root