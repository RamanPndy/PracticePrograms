class Node:
 
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0

def BTLeftView(root):
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
 