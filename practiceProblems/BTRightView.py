from collections import deque


class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.hd = 0

def BTRightView(root):
    if not root:
        return
    q = deque()
    q.append(root)

    while q:
         n =len(q) #number of nodes at current level

         for i in range(1, n+1):
             node = q.popleft()

             if i ==n :
                 print (node.val)

             if node.left:
                 q.append(node.left)

             if node.right:
                 q.append(node.right)

root = newNode(10)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(7)
root.left.right = newNode(8)
root.right.right = newNode(15)
root.right.left = newNode(12)
root.right.right.left = newNode(14)
BTRightView(root)