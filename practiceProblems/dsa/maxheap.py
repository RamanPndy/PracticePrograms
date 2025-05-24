class MaxHeap:
    '''
    A MaxHeap is a complete binary tree where the value of each node is greater than or equal to the values of its children.
    This implementation uses a list to represent the heap.
    The root node is at index 0, and for any node at index i:
    - The left child is at index 2*i + 1
    - The right child is at index 2*i + 2
    - The parent is at index (i - 1) // 2
    The time complexity for insertion and extraction is O(log n), where n is the number of elements in the heap.
    The space complexity is O(n) for storing the elements in the heap.
    The display method prints the heap in a list format.
    '''
    def __init__(self):
        self.heap = []

    def _parent(self, index): return (index - 1) // 2
    def _left(self, index): return 2 * index + 1
    def _right(self, index): return 2 * index + 2

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self._parent(i)]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def _heapify_down(self, i):
        largest = i
        left = self._left(i)
        right = self._right(i)
        n = len(self.heap)

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def display(self):
        print(self.heap)

h = MaxHeap()
h.insert(10)
h.insert(20)
h.insert(5)
h.insert(30)

h.display()  # Output: [30, 20, 5, 10]

print("Max:", h.extract_max())  # Output: 30
h.display()  # Output: [20, 10, 5]
