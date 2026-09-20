import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeKLists(self, lists):
        """
        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
        Merge all the linked-lists into one sorted linked-list and return it.

        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
        [
        1->4->5,
        1->3->4,
        2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6
        Question: Merge k sorted linked lists into one sorted linked list.
        Approach:
        - Use a min heap to always get the smallest current node among the k lists.
        - Initialize the heap with the first node of each list.
        - Pop the smallest node from the heap, add it to the merged list, and push the next node from the same list into the heap.
        - Continue until the heap is empty.
        Time Complexity: O(N log k) where N is the total number of nodes and k is the number of linked lists.
        Space Complexity: O(k) for the heap.
        Steps:
        1. create head node and put it to current node
        2. create min heap array
        3. traverse through each lists array
            - put list value and index in heap and proceed with next node
        4. traverse heap
            - get value and index from heap
            - add node with value in current node
            - proceed with next current node
            - if there is any list in lists array then append it to heap and proceed with next node
        5. return next of head
        """
        head = ListNode()
        curr = head
        heap = []
        # print(lists) [ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}, ListNode{val: 2, next: ListNode{val: 6, next: None}}]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        # print(heap) [(1, 0), (1, 1), (2, 2)]
        while heap:
            val, i = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next