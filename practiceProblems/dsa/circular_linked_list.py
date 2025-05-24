class Node:
    '''
    A class representing a node in a linked list.
    Each node contains a value and pointers to left and right children.
    TC: O(1) for node creation
    SC: O(1) for storing node properties
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    '''
    A class representing a circular linked list.
    Each node points to the next node, and the last node points back to the head.
    The list can be traversed starting from any node.
    TC: O(n) for append, prepend, and delete operations
    SC: O(n) for storing n nodes
    '''
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to itself, circular link
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def traverse(self):
        elements = []
        if not self.head:
            return elements
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        return elements

cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)

print(cll.traverse())  # Output: [1, 2, 3]

cll.prepend(0)
print(cll.traverse())  # Output: [0, 1, 2, 3]
