class HashNode:
    '''
    A node in the hash table linked list.
    Each node contains a key-value pair and a pointer to the next node.
    TC: O(1) for insertion, deletion, and search
    SC: O(1) for each node
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A simple hash table implementation using separate chaining for collision resolution.
    Each bucket is a linked list of HashNode objects.
    TC: O(1) for insertion, deletion, and search on average
    SC: O(n) for n elements in the hash table
    '''
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        head = self.buckets[index]

        # Check if key already exists, update value
        current = head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Insert new node at the head for simplicity
        new_node = HashNode(key, value)
        new_node.next = head
        self.buckets[index] = new_node
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Key not found

    def remove(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False  # Key not found

    def __len__(self):
        return self.size

ht = HashTable()

ht.put("apple", 10)
ht.put("banana", 20)
ht.put("orange", 30)

print(ht.get("banana"))  # Output: 20

ht.put("banana", 25)     # Update value
print(ht.get("banana"))  # Output: 25

ht.remove("apple")
print(ht.get("apple"))   # Output: None

print("Size:", len(ht))  # Output: 2
