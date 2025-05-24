class TreeNode:
    '''
    A simple tree node class that can have multiple children.
    Each node contains data and a list of children nodes.
    
    TC: O(1) for insertion
    SC: O(n) for storing children nodes
    '''
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print(" " * level * 2 + str(self.data))
        for child in self.children:
            child.display(level + 1)

class BinaryTreeNode:
    '''
    A simple binary tree node class that can have at most two children.
    Each node contains data, a left child, and a right child.
    TC: O(1) for insertion
    SC: O(1) for storing left and right children
    '''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def display(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self.data))
        if self.left:
            self.left.display(level + 1, "L--- ")
        if self.right:
            self.right.display(level + 1, "R--- ")

root = BinaryTreeNode(1)
left = root.insert_left(2)
right = root.insert_right(3)
left.insert_left(4)
left.insert_right(5)
right.insert_left(6)
right.insert_right(7)

root.display()
