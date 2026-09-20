# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Question:
        Reverse the given singly-linked list.

        Approach:
        - Use three pointers: prev, curr, and nxt to reverse the links iteratively.
        - Traverse the list and reverse the direction of the next pointers.

        Complexity Analysis:
        - Time: O(n) where n is the number of nodes in the linked list.
        - Space: O(1) since we only use a constant amount of extra space.

        Steps:
        1. Initialize prev as None and curr as head.
        2. Iterate through the list and reverse the next pointers.
        3. Return prev as the new head of the reversed list.
        """
        if not head:
            return
        
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
