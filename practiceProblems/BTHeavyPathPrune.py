class Node:

    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to remove all nodes which do not
# lie in th sum path
def prune(root, sum):
    # Base case
    if root is None:
        return None

    # Recur for left and right subtree
    root.left = prune(root.left, sum - root.data)
    root.right = prune(root.right, sum - root.data)

    # if node is leaf and sum is found greater
    # than data than remove node An important
    # thing to remember is that a non-leaf node
    # can become a leaf when its children are
    # removed
    if root.left is None and root.right is None:
        if sum > root.data:
            return None

    return root


# inorder traversal
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, "", end="")
    inorder(root.right)


def get_root():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(12)
    root.right.right.left = Node(10)
    root.right.right.left.right = Node(11)
    root.left.left.right.left = Node(13)
    root.left.left.right.right = Node(14)
    root.left.left.right.right.left = Node(15)
    return root


# Driver program to test above function
root = get_root()

print("Tree before truncation")
inorder(root)
prune(root, 45)
print("\nTree after truncation")
inorder(root)