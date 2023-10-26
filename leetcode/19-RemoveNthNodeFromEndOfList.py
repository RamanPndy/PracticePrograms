# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]
        """
        slow, fast = head, head
        # advance fast to nth position
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        #remove the node
        slow.next = slow.next.next
        return head