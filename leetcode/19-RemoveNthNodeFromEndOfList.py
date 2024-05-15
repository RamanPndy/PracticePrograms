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
        Steps:
        1. create 2 pointers slow and fast and point both to head
        2. while n is positive then move fast pointer
        3. if fast is None then return next of head
        4. then advance both fast and slow as now they are nth postions apart, when next of fast gets to None, 
            slow will be just before the item to be deleted
        5. remove the node i.e. next of slow becomes next of next of slow
        6. return head
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