from collections import deque
class Node:

    # A constructor for making a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def BTBoundry(root):
    if not root:
        return

    if not root.left and not root.right:
        print (root.data)
        return

    list = []
    list.append(root.data)

    temp = root.left
    while temp.left:
        list.append(temp.data)
        temp = temp.left

    q = deque()
    q.append(root)
    while q:
        x = q.pop()
        if not x.left and not x.right:
            list.append(x.data)
        if x.right:
            q.append(x.right)
        if x.left:
            q.append(x.left)

    temp = root.right
    while temp.right:
        list.append(temp.data)
        temp = temp.right

    print(list)


root = Node(20)

root.left = Node(8)
root.right = Node(22)

root.left.left = Node(4)
root.left.right = Node(12)

root.right.left = Node(10)
root.right.right = Node(25)

BTBoundry(root)