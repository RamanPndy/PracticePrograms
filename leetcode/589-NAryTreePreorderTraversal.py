'''
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Algorithm:
- Use a recursive approach to traverse the n-ary tree in preorder.
- Start from the root node and visit it first.
- Then recursively visit each child of the current node in order.
- Collect the values of the visited nodes in a list and return it.

'''

def preorder(root):
    '''
    Preorder traversal of an n-ary tree using recursion.
    Returns a list of node values in preorder.
    Example:
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [1,3,5,6,2,4]

    Time Complexity: O(N), where N is the number of nodes in the n-ary tree.
    Space Complexity: O(H), where H is the height of the n-ary tree (recursion stack).
    '''
    result = []
    
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        for child in node.children:
            dfs(child)

    dfs(root)
    return result

def preorder_iterative(root):
    '''
    Preorder traversal of an n-ary tree using iteration.
    Returns a list of node values in preorder.
    Example:
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [1,3,5,6,2,4]

    Algorithm:
    - Use a stack to simulate the recursion.
    - Start from the root node and push it onto the stack.
    - While the stack is not empty, pop a node, visit it, and push its children onto the stack in reverse order.
    - Collect the values of the visited nodes in a list and return it.

    Time Complexity: O(N), where N is the number of nodes in the n-ary tree.
    Space Complexity: O(H), where H is the height of the n-ary tree (stack).
    '''
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        stack.extend(reversed(node.children))
    return result