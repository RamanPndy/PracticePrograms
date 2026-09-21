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

        Question:

        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.
        Approach:
        - Initialize a carry variable to 0 and a dummy head for the result linked list.
        - Traverse both linked lists simultaneously, adding corresponding node values along with the carry.
        - Update the carry and the current node value accordingly.
        - Continue until both linked lists and the carry are exhausted.
        - Return the next of the dummy head as the result linked list.
        Complexity Analysis:
        - Time: O(max(m, n)) where m and n are the lengths of the two linked lists, as we traverse both lists once.
        - Space: O(max(m, n)) for the new linked list storing the result.
        Intuition:
        - The problem can be solved by simulating the addition process digit by digit, taking care of the carry at each step.
        - This approach ensures that we correctly handle the carry at each step and construct the resulting linked list in the correct order.
        - The dummy head simplifies the handling of the head of the result linked list, avoiding special cases for the first node.
        - The overall approach mimics the manual addition process, ensuring correctness and simplicity.
        Edge Cases:
        - If one of the linked lists is longer than the other, the remaining nodes are added along with the carry.
        - If there is a carry left after processing both linked lists, it is added as a new node at the end of the result linked list.
        - If both linked lists are empty, the result is an empty linked list (or a single node with value 0).
        Example Walkthrough:
        For l1 = [2,4,3] and l2 = [5,6,4], the addition will proceed as follows:
        1. Add 2 + 5 = 7, no carry, result = [7]
        2. Add 4 + 6 = 10, carry = 1, result = [7,0]
        3. Add 3 + 4 + 1 (carry) = 8, no carry, result = [7,0,8]
        The walkthrough demonstrates how the addition is performed digit by digit, taking care of the carry at each step.
        - This example helps in understanding how the carry is propagated and how the result linked list is constructed step by step.
        - This section provides a step-by-step guide to implementing the solution in code.
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