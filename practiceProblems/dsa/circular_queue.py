class CircularQueue:
    '''
    Circular Queue implementation using a fixed-size array.
    This implementation allows for efficient use of space by reusing empty slots.
    It supports basic operations: enqueue, dequeue, peek, is_empty, is_full, and display.
    TC: O(1) for all operations
    SC: O(n) for storing elements in the queue
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # fixed size
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"Enqueued {item}.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        item = self.queue[self.front]
        if self.front == self.rear:
            # Queue has only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Queue (front -> rear): ", end="")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)  # should indicate full

cq.display()

print("Dequeued:", cq.dequeue())
cq.enqueue(60)  # should now be possible
cq.display()

print("Front item:", cq.peek())
