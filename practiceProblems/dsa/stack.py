class Stack:
    '''
    A simple stack implementation using a list in Python.
    Supports basic operations: push, pop, peek, is_empty, size, and display.
    TC: O(1) for push and pop operations
    SC: O(n) for storing n elements
    '''
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack (top -> bottom):", self.stack[::-1])

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Top of stack:", s.peek())
print("Popped item:", s.pop())
s.display()