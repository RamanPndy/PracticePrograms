# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        Input: root = [5,3,6,2,4,null,null,1], k = 3
        Output: 3
        Steps:
        1. Perform a level-order traversal (BFS) to collect all node values in a list.
        2. Sort the list of node values.
        3. Return the k-th smallest element from the sorted list.
        """
        if root is None:
            return 0
        q = [root]
        a = []
        while q:
            node = q.pop(0)
            a.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        a = sorted(a)
        return a[k-1]