class Node:
 
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0

def BTLeftView(root):
    """
    Print the left view of a binary tree.

    :param root: Root node of the binary tree
    :return: None (prints the left view)
    Time Complexity: O(n) where n is the number of nodes in the binary tree.
    Space Complexity: O(n) for the queue used to store nodes at each level.
    Steps:
    - Perform a level order traversal of the binary tree using a queue.
    - For each level, append the first node's value to the result list.
    - Add the left and right children of each node to the queue.
    - Continue until all levels are processed.
    - Print the result list containing the left view of the binary tree.
    """
    if not root:
        return

    q = []
    res = []
    q.append(root)

    while (len(q)):
 
        # number of nodes at current level
        n = len(q)
 
        # Traverse all nodes of current level
        for i in range(1, n + 1):
            temp = q.pop(0)

            # append the left most element
            # at the level
            if (i == 1):
                res.append(temp.data)
 
            # Add left node to queue
            if temp.left:
                q.append(temp.left)
 
            # Add right node to queue
            if temp.right:
                q.append(temp.right)

    for val in res:
        print(val)
 