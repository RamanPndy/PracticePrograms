# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        Question: Find the next greater node for each node in a linked list.
        Approach: Use a stack to keep track of nodes for which we haven't found the next greater node yet. 
        Iterate through the linked list, and for each node, pop elements from the stack,
        if the current node's value is greater than the value of the node at the top of the stack. Update the result list accordingly.
        Finally, any nodes left in the stack do not have a next greater node, so their values remain 0 in the result list.
        Time Complexity: O(n), where n is the number of nodes in the linked list, because each node is pushed and popped from the stack at most once.
        Space Complexity: O(n), for the stack and the result list.
        Example:
        Input: head = [2,1,5]
        Output: [5,5,0]
        Explanation: The next larger node for 2 is 5, for 1 is 5, and for 5 there is no larger node, so it is 0.
        Another Example:
        Input: head = [1,7,5,1,9,2,5,1]
        Output: [7,9,9,9,0,5,0,0]
        Explanation: The next larger node for 1 is 7, for 7 is 9, for 5 is 9, for 1 is 9, for 9 there is no larger node, for 2 is 5, for 5 there is no larger node, and for 1 there is no larger node, so it is 0.
        Steps:
        1. Initialize an empty result list and an empty stack.
        2. Traverse the linked list node by node.
        3. For each node, while the stack is not empty and the current node's value is greater than the value of the node at the top of the stack, 
        pop the stack and update the corresponding index in the result list with the current node's value.
        4. Push the current node's index and value onto the stack.
        5. Append 0 to the result list (default value if no greater node is found).
        6. Move to the next node in the linked list.
        7. Return the result list after the traversal is complete.
        """
        res, stack = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                topOfStack = stack.pop()
                res[topOfStack[0]] = head.val
            stack.append([len(res), head.val])
            res.append(0)
            head = head.next
        return res