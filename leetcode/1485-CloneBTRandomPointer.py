'''
By using a hashmap to maintain a correspondence between the original nodes and the copied nodes, we ensure that the 
random pointers get correctly assigned even if the target nodes are copied later during the DFS traversal.

The algorithm works as follows:
1. Start at the root of the original tree.
2. If the current node is null, return null, as there's nothing to copy.
3. If the current node's copy already exists in the hashmap, return the copy to avoid duplication.
4. If the copy does not exist yet, create a new NodeCopy instance with the same value.
5. Store the new NodeCopy instance in the hashmap, with the original node as the key.
6. Set the left and right child pointers for the NodeCopy by recursively calling our DFS function.
7. Set the random pointer for the NodeCopy in a similar fashion, by calling DFS for the original node's random pointer and using the hashmap for reference.
8. After the recursion completes, return the copy of the root node which now represents the root of the deep-copied tree.
'''

# Definition for a Node with an additional random pointer.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


# Definition for a NodeCopy, which is used to represent the cloned tree.
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        # Helper function to perform a deep copy of the tree using DFS
        def dfs_clone(node):
            # Base case: If the current node is None, return None
            if node is None:
                return None
          
            # If we have already cloned this node, return its clone from the map
            if node in clone_map:
                return clone_map[node]
          
            # Create a new NodeCopy for the current node
            cloned_node = NodeCopy(node.val)
          
            # Save this cloned node in the map with the original node as the key
            clone_map[node] = cloned_node
          
            # Recursively clone the left subtree
            cloned_node.left = dfs_clone(node.left)
          
            # Recursively clone the right subtree
            cloned_node.right = dfs_clone(node.right)
          
            # Recursively clone the random pointer
            cloned_node.random = dfs_clone(node.random)
          
            # Return the cloned node
            return cloned_node
      
        # Initialize a map to keep track of original node to its cloned counterpart
        clone_map = {}
      
        # Kick off the cloning process starting from the root of the tree
        return dfs_clone(root)