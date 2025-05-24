class MinHeap:
    '''
    MinHeap implementation in Python
    This implementation uses a list to represent the heap.
    The root node is at index 0, and for any node at index i:
    - The left child is at index 2*i + 1
    - The right child is at index 2*i + 2
    - The parent is at index (i - 1) // 2
    The time complexity for insertion and extraction is O(log n), where n is the number of elements in the heap.
    The space complexity is O(n) for storing the elements in the heap.
    The display method prints the heap in a list format.
    This implementation supports basic operations: insert, extract_min, and display.
    '''
    def __init__(self):
        self.heap = []

    def _parent(self, index): return (index - 1) // 2
    def _left(self, index): return 2 * index + 1
    def _right(self, index): return 2 * index + 2

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def _heapify_down(self, i):
        smallest = i
        left = self._left(i)
        right = self._right(i)
        n = len(self.heap)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def display(self):
        print(self.heap)

h = MinHeap()
h.insert(10)
h.insert(4)
h.insert(15)
h.insert(2)

h.display()  # Output: [2, 4, 15, 10]

print("Min:", h.extract_min())  # Output: 2
h.display()  # Output: [4, 10, 15]
