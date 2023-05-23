# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            a, b = current.next, current.next.next
            a.next = b.next
            b.next = a
            current.next = b
            current = current.next.next
        return dummy.next