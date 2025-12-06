'''
Given a stream of numbers, find nth recurring recently used number. Example - [1, 1, 2, 3, 2, 4] Suppose n = 2

Explanation:
1.Track frequency of each number
2.Track most recent index of each number
3.Keep only numbers with frequency > 1 (recurring)
4.Sort by last seen index
5.Return the n-th most recent
'''

def nth_recent_recurring(stream, n):
    last_seen = {}         # number -> last index
    count = {}             # number -> frequency
    
    for i, num in enumerate(stream):
        count[num] = count.get(num, 0) + 1
        last_seen[num] = i  # update last seen position

    # Filter only numbers that occurred more than once (recurring)
    recurring = [num for num in last_seen if count[num] > 1]

    # Sort by last seen timestamp (most recent first)
    recurring.sort(key=lambda x: last_seen[x], reverse=True)

    # If n is within bounds, return nth recurring
    return recurring[n-1] if n <= len(recurring) else None


# Example
stream = [1, 1, 2, 3, 2, 4]
n = 2

print(nth_recent_recurring(stream, n))  # Output: 1

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class RecentRecurring:
    '''
    LRU implementation
    ✔ Insert number in O(1)
    ✔ Update recency in O(1)
    ✔ Query nth recurring in O(n) (only traversal)
    '''
    def __init__(self):
        self.count = {}        # num -> frequency
        self.nodes = {}        # num -> Node in LRU list (only if recurring)
        
        # Dummy head & tail for doubly linked list
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---- Doubly linked list helpers ----
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # ---- Stream update in O(1) ----
    def add(self, num):
        self.count[num] = self.count.get(num, 0) + 1
        
        # First occurrence → do nothing
        if self.count[num] == 1:
            return
        
        # Second occurrence → add to recurring LRU list
        if self.count[num] == 2:
            node = Node(num)
            self.nodes[num] = node
            self._insert_front(node)
            return
        
        # More occurrences → move node to front
        node = self.nodes[num]
        self._remove(node)
        self._insert_front(node)

    # ---- Query nth most recent recurring ----
    def nth_recent(self, n):
        current = self.head.next
        i = 1
        while current != self.tail:
            if i == n:
                return current.val
            current = current.next
            i += 1
        return None
