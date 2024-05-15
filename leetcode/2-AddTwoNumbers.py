# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
        Steps:
        1. creates vars carry to store carry and result which would be linked list
        2. traverse both list and carry simulteneously
            1. create sum of node values of both list and carry
            2. recalculate carry by carry = sum // 10
            3. update sum by sum = sum % 10
            4. create new node from updated sum and assign it to next of result list
            5. move forward result list and both list
        3. next of reuslt list would be answer list.
        """
        carry = 0
        result = ListNode(0)
        p = result

        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            s= n1 + n2 + carry
            carry = s // 10
            s = s % 10
            p.next = ListNode(s)

            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next