# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Question: Can you return the zigzag level order traversal of a binary tree's nodes' values? (i.e., from left to right, then right to left for the next level and alternate between).
        Approach:
        - Use a queue to perform a level order traversal (BFS) of the binary tree.
        - Keep track of the current direction (left to right or right to left) using a variable.
        - For each level, collect the node values and reverse the order if needed based on the current direction.
        - Append the collected level values to the result list.
        - Toggle the direction for the next level.
        - Return the result list after traversing all levels.
        Time Complexity: O(n), where n is the number of nodes in the binary tree.
        Space Complexity: O(n), due to the queue used for level order traversal.
        Steps:
        1. Check if the root is None, return an empty list if true.
        2. Initialize a queue with the root node and a direction variable.
        3. While the queue is not empty, process each level:
            a. Initialize an empty list for the current level.
            b. Iterate through the nodes in the current level, appending their values to the level list and adding their children to the queue.
            c. Reverse the level list if the direction is right to left.
            d. Append the level list to the result list.
            e. Toggle the direction for the next level.
        4. Return the result list.
        """
        if not root:
            return
        q = [root]
        direction = 1
        res = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level = level[::direction]
            direction = -1 * direction
            res.append(level)
        return res