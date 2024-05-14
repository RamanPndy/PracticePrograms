class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

        Steps:
        1. create a map which will hold node to node mapping.
        2. create variable curr and assign head to it.
        3. traverse while current is not None:
            - map[cuurent_node] = Node(current.value)
            - proceed current
        4. again assign head to curr.
        5. traverse while current is not None:
            - get the copy node from map
            - assign next of current node from map to next of copy
            - assing random of current node from map to random of copy
            - proceed current
        6. return map[head]
        """
        if not head:
            return
        m = {None : None}
        curr = head
        while curr:
            m[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = m[curr]
            copy.next = m[curr.next]
            copy.random = m[curr.random]
            curr = curr.next
        return m[head]