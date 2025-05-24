class Queue:
    '''
    A simple queue implementation using a list.
    Supports basic operations: enqueue, dequeue, peek, is_empty, size, and display.
    TC: O(1) for enqueue and O(n) for dequeue
    SC: O(n) for storing n elements
    '''
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item}.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.queue.pop(0)  # O(n) operation

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue (front -> rear):", self.queue)

q = Queue()
q.enqueue(5)
q.enqueue(15)
q.enqueue(25)
q.display()
print("Front item:", q.peek())
print("Dequeued item:", q.dequeue())
q.display()
