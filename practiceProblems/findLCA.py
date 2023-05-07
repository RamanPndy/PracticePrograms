#find LCA in a Binary Search Tree

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def LCA (root,n1,n2):
    #base case
    if root == None:
        return False

    # If both n1 and n2 are smaller than root then these lies in left subtree
    if(root.key > n1 and root.key > n2):
        return LCA(root.left,n1,n2)

    #If both n1 and n2 are greater than root then these lies in right subtree
    if(root.key < n1 and root.key < n2):
        return LCA(root.right,n1,n2)

