from collections import deque


class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.hd = 0

def BTTopView(root):
    if not root:
        return
    hd = 0
    root.hd = hd
    m = dict()
    q = deque()
    q.append(root)

    while(q):
        node = q.popleft()

        hd = node.hd

        if hd not in m:
            m[hd] = node.val

        if node.left:
            node.left.hd = hd -1
            q.append(node.left)

        if node.right:
            node.right.hd = hd +1
            q.append(node.right)

    for i in sorted(m):
        print (m[i])

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.right = newNode(4)
root.left.right.right = newNode(5)
root.left.right.right.right = newNode(6)
print("Following are nodes in top",  "view of Binary Tree")
BTTopView(root)