class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def findDistance(root,n1,n2):
    x = PathLength(root,n1) - 1
    y = PathLength(root,n2) - 1

    lcaData = findLCA(root,n1,n2).data
    lcaDistance = PathLength(root,lcaData) - 1
    return (x + y )- 2* lcaDistance

def PathLength(root,n1):
    if root != None:
        x = 0
        y = PathLength(root.left,n1)
        z = PathLength(root.left,n1)
        if (root.data == n1 or (y > 0) or (z > 0)):
            return x+1
        return 0
    return 0

def findLCA(root,n1,n2):
    if root != None:
        if((root.data == n1) or (root.data == n2)):
            return root
        left = findLCA(root.left,n1,n2)
        right = findLCA(root.right,n1,n2)

        if((left !=  None) and (right != None)):
            return root

        if (left != None):
            return left

        if(right != None):
            return right
    return None

root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(25)
root.right.left = Node(30)
root.right.right = Node(35)

print findDistance(root,10,30)