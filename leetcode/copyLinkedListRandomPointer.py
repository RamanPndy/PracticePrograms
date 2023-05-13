"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
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