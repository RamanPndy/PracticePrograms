# level order traversal of Binary Tree
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def printLevelOrder(root):
	h = height(root)
	for d in range(1,h+1):
		printGivenLevel(root,d)

def printGivenLevel(root,level):
	if root is None:
		return
	if level == 1:
		print "%d" %(root.data),
	elif level > 1:
		printGivenLevel(root.left,level-1)
		printGivenLevel(root.right,level-1)

def height(node):
	if node is None:
		return 0
	else:
		# compute the hegith of each subtree
		lheight = height(node.left)
		rheight = height(node.right)

		# use the larger one
		if lheight > rheight:
			return lheight+1
		else:
			return rheight+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)

printLevelOrder(root)
