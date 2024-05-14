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
        Input: head = [1,2,3,4]
        Output: [2,1,4,3]
        Steps:
        1. create dummy node and assign head to next of dummy node
        2. create current node and assign dummy to current node
        3. traverse while next and next of next of current node is not None
            - creates vars a and b which will hold next of current and next of next of current respectively
            - assign next of b to next of a
            - assign a to next of b
            - assign b to next of current
            - proceed current to 2 steps ie. next of next of current
        4. return next of dummy
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