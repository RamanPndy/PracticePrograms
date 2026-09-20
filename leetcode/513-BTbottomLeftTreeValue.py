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
        Question: Find the leftmost value in the last row of the binary tree.
        Intuition: Perform a level-order traversal (BFS) and keep track of the first node in each level. 
        The last recorded first node will be the leftmost node in the bottom row.
        Steps:
        1. Initialize a queue with the root node.
        2. Initialize a variable to store the leftmost node value.
        3. While the queue is not empty, traverse all nodes at the current level.
        4. Update the leftmost node value with the first node of the current level.
        5. Add the right and left children of the current node to the queue (right first to ensure leftmost node is processed last).
        6. Return the leftmost node value after the traversal is complete.
        Time Complexity: O(n), where n is the number of nodes in the tree, as each node is processed once.
        Space Complexity: O(m), where m is the maximum number of nodes at any level (width of the tree).
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
        