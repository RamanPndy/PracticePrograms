# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Input: root = [1,2,3,4,null,5,6,null,null,7]
        Output: 7
        """
        if not root:
            return
        q = [root]
        # Initialize a variable to store the leftmost node value
        lft_most_val = 0
        # Perform level-order traversal
        while q:
            # Traverse all the nodes in the current level
            for _ in range(len(q)):
                # Dequeue the front node from the queue
                node = q.pop(0)
                # Update the leftmost node value if the current node is in the leftmost position of the current level
                lft_most_val = node.val
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return lft_most_val
        