RED = True
BLACK = False

class Node:
    '''
    A class to represent a node in a Red-Black Tree.
    Each node has a value, color (RED or BLACK), and pointers to its left child,
    right child, and parent.
    TC: O(1) for node creation
    SC: O(1) for storing node properties
    '''
    def __init__(self, val, color=RED, left=None, right=None, parent=None):
        self.val = val
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    '''
    A class to represent a Red-Black Tree.
    The tree maintains the Red-Black properties:
    1. Each node is either red or black.
    2. The root is always black.
    3. Red nodes cannot have red children (no two reds in a row).
    4. Every path from a node to its descendant NIL nodes must have the same number of black nodes.
    5. NIL nodes are considered black.
    The tree supports insertion and maintains the Red-Black properties.
    TC: O(log n) for insertion
    SC: O(n) for storing nodes
    '''
    def __init__(self):
        self.NIL = Node(val=None, color=BLACK)  # Sentinel NIL node
        self.root = self.NIL

    def insert(self, val):
        new_node = Node(val=val, color=RED, left=self.NIL, right=self.NIL, parent=None)
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.val < current.val:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node.parent and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    # Case 1: Uncle red
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Node is right child
                        node = node.parent
                        self.left_rotate(node)
                    # Case 3: Node is left child
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    # Mirror Case 1
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Mirror Case 2
                        node = node.parent
                        self.right_rotate(node)
                    # Mirror Case 3
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)
        self.root.color = BLACK

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def inorder_helper(self, node):
        if node != self.NIL:
            self.inorder_helper(node.left)
            print(f"{node.val} ({'R' if node.color == RED else 'B'})", end=" ")
            self.inorder_helper(node.right)

    def inorder(self):
        self.inorder_helper(self.root)
        print()

rbt = RedBlackTree()
for val in [20, 15, 25, 10, 5, 1, 30]:
    rbt.insert(val)

rbt.inorder()
