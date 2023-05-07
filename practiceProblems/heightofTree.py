class Node:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

def getHeight(root):
    q = []
    if root is None:
        return 0
    else:
        q.append(root)
        height = 0
        while True:
            nodeCount = len(q)

            if nodeCount == 0:
                return height

            height += 1

            while nodeCount > 0:
                node = q.pop(0)
                if node.lefchild:
                    q.append(node.lefchild)
                else:
                    q.append(node.rightchild)
                nodeCount -= 1
    return height

