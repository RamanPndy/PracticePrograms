# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        Input: head = [1,2,3,4]
        Output: [1,4,2,3]   
        Question:
        Reorder the given singly-linked list in the specific order: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

        Approach:
        - Find the middle of the linked list using the slow and fast pointer technique.
        - Reverse the second half of the list.
        - Merge the two halves by alternating nodes from each half.

        Complexity Analysis:
        - Time: O(n) where n is the number of nodes in the linked list.
        - Space: O(1) since we only use a constant amount of extra space.

        Steps:
        1. Use slow and fast pointers to find the middle of the list.
        2. Reverse the second half of the list.
        3. Merge the first half and the reversed second half alternately.
        """
        if not head:
            return
         
        fast, slow = head, head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        mid = slow
        
        # ------------------------------------------
        # Reverse second half
        
        prev, cur = None, mid
        
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        head_of_second_rev = prev
        
        # ------------------------------------------
        # Update link between first half and reversed second half
        
        first, second = head, head_of_second_rev
        
        while second.next:
            next_hop = first.next
            first.next = second
            first = next_hop
            
            next_hop = second.next
            second.next = first
            second = next_hop