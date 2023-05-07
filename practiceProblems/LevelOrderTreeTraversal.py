class Q:
    def __init__(self):
        self.q = []

    def getSize(self):
        return len(self.q)

    def enqueue(self,data):
        self.q.append(data)

    def dequeue(self):
        return self.q.pop(0)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return
    q = Q()
    q.enqueue(root)
    while q.getSize()>0:
        temp = q.dequeue()
        print temp.data
        if temp.left is not None:
            q.enqueue(temp.left)
        if temp.right is not None:
            q.enqueue(temp.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)