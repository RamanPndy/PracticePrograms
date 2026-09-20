class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Question: Can you find the maximum depth of a binary tree?
        Approach:
        - Use a queue to perform a level order traversal (BFS) of the binary tree.
        - Keep track of the depth by incrementing it at each level.
        - Return the depth after traversing all levels.
        Time Complexity: O(n), where n is the number of nodes in the binary tree.
        Space Complexity: O(n), due to the queue used for level order traversal.
        Steps:
        1. Initialize the depth to 0.
        2. Initialize the queue with the root node if it exists.
        3. While the queue is not empty, process each level:
            a. Increment the depth.
            b. Initialize an empty list for the next level.
            c. Iterate through the nodes in the current level, adding their children to the next level list.
            d. Update the queue with the next level list.
        4. Return the depth.
        """
        depth = 0
        q = [root] if root else []
        while q:
            depth += 1
            level = []
            for node in q:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            q = level
            
        return depth
