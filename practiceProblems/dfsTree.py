# DFS Tree Traversal
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def preOrder(root):
	if root is None:
		return
	if root is not None:
		print root.data
		preOrder(root.left)
		preOrder(root.right)

def inOrder(root):
	if root is None:
		return
	if root is not None:
		inOrder(root.left)
		print root.data
		inOrder(root.right)

def postOrder(root):
	if root is None:
		return
	if root is not None:
		postOrder(root.left)
		postOrder(root.right)
		print root.data

root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
print "Preorder traversal of binary tree is"
preOrder(root)
 
print "\nInorder traversal of binary tree is"
inOrder(root)
 
print "\nPostorder traversal of binary tree is"
postOrder(root)