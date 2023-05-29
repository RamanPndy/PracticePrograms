# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        Input: head = [1,2,3,4,5], k = 2
        Output: [1,4,3,2,5]
        Initialize three pointers: node1, node2, and fast to point to the head of the linked list.
        Move node1 and fast k-1 steps forward in the linked list.
        Move node2 and fast forward until fast reaches the end of the linked list.
        Swap the values of node1 and node2.
        Return the head of the modified linked list.
        """
        node1 = node2 = fast = head

        #Finding kth node from the start 
        k-=1
        while (k):
            node1 = node1.next
            fast = fast.next
            k-=1

        #Finding kth node from the end
        while (fast and fast.next):
            node2 = node2.next
            fast = fast.next

        #Swapping the values only
        temp = node1.val
        node1.val = node2.val
        node2.val = temp

        return head