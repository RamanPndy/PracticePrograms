'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Algorithm:
- Traverse the linked list and reverse every k nodes.
- If the number of remaining nodes is less than k, leave them as is.
- Use a dummy node to simplify edge cases.
- Maintain pointers to the previous group's tail and the current group's head.
- Reverse the nodes within each group and update the pointers accordingly.

Time Complexity: O(N), where N is the number of nodes in the linked list.
Space Complexity: O(1), as we are only using a constant amount of extra space.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            kth = prev_group
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next

            # Reverse the group
            prev, curr = kth.next, prev_group.next
            for i in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp