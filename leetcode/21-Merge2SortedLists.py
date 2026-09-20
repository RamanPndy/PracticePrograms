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
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        Question: Given the heads of two sorted linked lists, merge them into a single sorted linked list and return its head.
        Approach:
        - Create a dummy head node to simplify edge cases.
        - Use a current pointer to build the new list.
        - Traverse both lists, always appending the smaller node to the current pointer.
        - Once one list is exhausted, append the remaining nodes of the other list.
        - Return the next of the dummy head as the merged list.
        Time Complexity: O(n + m) where n and m are the lengths of the two lists.
        Space Complexity: O(1) as we are reusing the existing nodes.
        Steps:
        1. create a head pointer from Node definition
        2. create current pointer which points to head
        3. traverse through both lists
            - if list1.val < list2.val then append node from list1 to next of current and proceed list1
            - else append node from list2 to next of current and proceed list2
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