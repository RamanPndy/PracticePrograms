# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        postorder.pop(-1)

        if preorder:
            root_index_in_postorder = postorder.index(preorder[0])
            root.left = self.constructFromPrePost(preorder[:root_index_in_postorder+1], postorder[:root_index_in_postorder+1])
            root.right = self.constructFromPrePost(preorder[root_index_in_postorder+1:], postorder[root_index_in_postorder+1:])

        return root