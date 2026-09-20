class Node(object):
    def __init__(self, key, val):
        self.key =key
        self.val = val
        self.prev = self.next = None

class LRUCache(object):
    """
    LRU Cache implementation using a doubly linked list and a dictionary.

    - The doubly linked list maintains the order of usage, with the most recently used node at the right end and the least recently used node at the left end.
    - The dictionary provides O(1) access to nodes based on their keys.
    - The `insert` method adds a node to the right end of the list.
    - The `remove` method removes a node from the list.
    - The `get` method retrieves the value of a key if it exists in the cache and moves the corresponding node to the right end.
    - The `put` method adds a new key-value pair to the cache, removes the least recently used node if the cache exceeds its capacity, and moves the new node to the right end.
    Time Complexity:
    - `get` and `put` operations are O(1).
    Space Complexity:
    - O(capacity) for storing the nodes in the dictionary and the doubly linked list.
    Interview Implementation Notes:
    - This LRU Cache implementation is commonly asked in system design and coding interviews.
    - It demonstrates the use of a doubly linked list combined with a dictionary to achieve O(1) time complexity for both get and put operations.
    - The use of dummy nodes simplifies the insertion and removal operations by avoiding edge cases for the head and tail of the list.
    - This implementation ensures that both the get and put operations have a consistent O(1) time complexity, which is crucial for high-performance caching scenarios.
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}

        # Initialize the dummy left and right nodes of the doubly linked list.
        self.left , self.right = Node(0, 0), Node(0, 0)
        # Connect the dummy nodes to each other.
        self.left.next , self.right.prev = self.right, self.left
        

    def insert(self, node):
        """
        Insert a node at the right end of the doubly linked list.

        :param node: Node to be inserted
        :return: None
        """
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev ,nxt
    
    def remove(self, node):
        """
        Remove a node from the doubly linked list.

        :param node: Node to be removed
        :return: None
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        Retrieve the value of a key if it exists in the cache and move the corresponding node to the right end.
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        Add a new key-value pair to the cache, remove the least recently used node if the cache exceeds its capacity, and move the new node to the right end.
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Remove the least recently used node if the cache exceeds its capacity.
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)