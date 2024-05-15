# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        Problem : Given the root of a binary tree, flatten the tree into a "linked list":
        The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
        The "linked list" should be in the same order as a pre-order traversal of the binary tree.

        Input: root = [1,2,5,3,4,null,6]
        Output: [1,null,2,null,3,null,4,null,5,null,6]

        TC: O(n)
        SC: O(h)

        Steps:
        1. do recursive traversal of tree and return last node which would be tail of list.
        2. get left and right tail of left and right subtrees.
        3. if leftTail is not None:
            a. assign right of the root to right of left tail. now right of the left tail and right of the root points to same node.
            b. now to flatten the tree we need to put left of the root to in between of root and right of the root so right of
               the root will now point to left of the root.
            c. after this there should not be any left node for the root so left of root becomes None
        4. tail of list will be right most node of the root ie. rightTail
        5. if rightTail is None but leftTail is not None in that case leftTail will become tail of list
        6. if both rightTail and leftTail becomes None then root will become the tail of list.
        """
        # recursively traverse tree and return tail of list
        def dfs(root):
            if not root:
                return None

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if leftTail:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            last = rightTail or leftTail or root
            return last
        dfs(root)