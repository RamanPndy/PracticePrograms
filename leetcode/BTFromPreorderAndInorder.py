# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        preorder traversal provides us with the placement of the root
        inorder traversal provides us with the placement of the left and right children
        """
        if not preorder or not inorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        root_index_in_preorder = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:root_index_in_preorder + 1], inorder[:root_index_in_preorder])
        root.right = self.buildTree(preorder[root_index_in_preorder + 1:], inorder[root_index_in_preorder + 1:])

        return root