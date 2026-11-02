# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        Question:
        Given the head of a linked list, rotate the list to the right by k places.

        Example:
        Input: head = [1,2,3,4,5], k = 2
        Output: [4,5,1,2,3]

        Approach:
        1. Compute the length of the linked list.
        2. Make the list circular by connecting the last node to the head.
        3. Find the new head after rotation by moving (length - k % length) steps from the current head.
        4. Break the circular link to form the rotated list.

        Why this works:
        By making the list circular and then breaking it at the correct position, 
        we effectively rotate the list to the right by k places.

        Time complexity:
        O(n) where n is the number of nodes in the linked list.

        Space complexity:
        O(1) as we are using constant extra space.
        """
        if not head or not head.next or k == 0:
            return head

        # Compute the length of the list and get the last node
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1

        # Make the list circular
        last.next = head

        # Find the new head after rotation
        k = k % length
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        return new_head
        