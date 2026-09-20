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

        Question: How can we swap the kth node from the beginning with the kth node from the end in a singly-linked list?
        Intuition: By using two pointers and moving them appropriately, we can identify the kth node from the beginning and the kth node from the end 
        efficiently without needing to traverse the list multiple times.
        Steps:
        1. Initialize three pointers: node1, node2, and fast to point to the head of the linked list.
        2. Move node1 and fast k-1 steps forward in the linked list.
        3. Move node2 and fast forward until fast reaches the end of the linked list.
        4. Swap the values of node1 and node2.
        5. Return the head of the modified linked list.
        Time Complexity: O(n), where n is the number of nodes in the linked list, as we traverse the list at most twice.
        Space Complexity: O(1), as we only use a constant amount of extra space for the pointers.
        Interview Explanation: The key insight is to use two pointers to efficiently locate the kth node from the beginning and the kth node from the end. 
        By moving one pointer k-1 steps ahead and then advancing both pointers until the fast pointer reaches the end, we can identify the nodes to swap 
        without needing multiple passes through the list.
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