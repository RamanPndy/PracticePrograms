import heapq

class PriorityQueue:
    '''
    A simple implementation of a priority queue using heapq.
    This implementation allows for efficient retrieval of the highest priority item.
    It supports basic operations: push, pop, peek, is_empty, and size.
    TC: O(log n) for push and pop operations
    SC: O(n) for storing elements in the priority queue
    '''
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        # heapq is a min-heap, so lower priority value means higher priority
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if self.heap:
            priority, item = heapq.heappop(self.heap)
            return item
        raise IndexError("pop from empty priority queue")

    def peek(self):
        if self.heap:
            return self.heap[0][1]
        raise IndexError("peek from empty priority queue")

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

pq = PriorityQueue()
pq.push("task1", priority=3)
pq.push("task2", priority=1)
pq.push("task3", priority=2)

while not pq.is_empty():
    print(pq.pop())

# Output:
# task2
# task3
# task1
