class Node:
    '''
    A class representing a node in a tree.
    Each node contains a value and pointers to left and right children.
    TC: O(1) for node creation
    SC: O(1) for storing node properties
    '''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    '''
    Inorder traversal of a binary tree.
    Inorder traversal visits the left subtree, the root node, and then the right subtree.
    TC: O(n) for visiting all nodes
    SC: O(h) for the recursion stack, where h is the height of the tree
    '''
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def preorder(root):
    '''
    Preorder traversal of a binary tree.
    Preorder traversal visits the root node, then the left subtree, and finally the right subtree.
    TC: O(n) for visiting all nodes
    SC: O(h) for the recursion stack, where h is the height of the tree
    '''
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    '''
    Postorder traversal of a binary tree.
    Postorder traversal visits the left subtree, then the right subtree, and finally the root node.
    TC: O(n) for visiting all nodes
    SC: O(h) for the recursion stack, where h is the height of the tree
    '''
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

# Creating a sample tree:
#         1
#       /   \
#      2     3
#     / \   /
#    4   5 6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print("Inorder traversal:")
inorder(root)      # Output: 4 2 5 1 6 3
print("\nPreorder traversal:")
preorder(root)     # Output: 1 2 4 5 3 6
print("\nPostorder traversal:")
postorder(root)    # Output: 4 5 2 6 3 1
