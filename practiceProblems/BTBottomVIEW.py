from collections import deque


class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.hd = 0

def BTBottomView(root):
    if not root:
        return
    hd = 0
    root.hd = hd
    m = dict()
    q = deque()
    q.append(root)

    while (q):
        node = q.popleft()

        hd = node.hd

        m[hd] = node.val

        if node.left:
            node.left.hd = hd - 1
            q.append(node.left)

        if node.right:
            node.right.hd = hd + 1
            q.append(node.right)

    for i in sorted(m):
        print(m[i])

root = newNode(20)
root.left = newNode(8);
root.right = newNode(22);
root.left.left = newNode(5);
root.left.right = newNode(3);
root.right.left = newNode(4);
root.right.right = newNode(25);
root.left.right.left = newNode(10);
root.left.right.right = newNode(14);
print("Following are nodes in Bottom",  "view of Binary Tree")
BTBottomView(root)