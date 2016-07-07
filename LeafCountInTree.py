class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def getValue(self):
        return self.val

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right


class Tree:
    def __init__(self,data):
        self.root = Node(data)

    def getLeafCount(self):
        if self.root == None:
            return 0
        elif self.root.left == None and self.root.right == None:
            return 1
        else :
            return self.getLeafCount(self.root.left) + self.getLeafCount(self.root.right)

if __name__ == "__main__":
    t = Tree(5)
    t.root.right = Tree(7)
    t.root.left = Tree(2)
    t.root.left.left = Tree(3)
    t.root.left.right = Tree(6)
    print t.getLeafCount()