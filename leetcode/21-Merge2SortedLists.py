# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        Steps:
        1. create a head pointer from Node definition
        2. create current pointer which points to head
        3. traverse through both lists
            - if list1.val < list2.val then append node from list1 to next of current and proceed list1
            - else append node from list2 to next of current and proceed list1
            proceed current to next as well
        4. once loop ends assign remaining nodes from list1 or list2 to next of current
        5. retun next of head
        """
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
        return head.next