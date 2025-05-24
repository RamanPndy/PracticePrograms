class Node:
    '''Node class for linked list'''
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node

class LinkedList:
    '''
    A simple singly linked list implementation.
    Supports basic operations: append, prepend, insert after a node,
    delete a node, and display the list.
    TC: O(n) for append, prepend, and delete operations
    SC: O(n) for storing n nodes
    '''
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node at the end"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """Add a node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node_data, data):
        """Insert after a specific node"""
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if not current:
            print(f"Node with data {prev_node_data} not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, key):
        """Delete the first occurrence of a node by value"""
        current = self.head

        # If head node is to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with value {key} not found.")
            return

        prev.next = current.next
        current = None

    def display(self):
        """Print the linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.insert_after_node(10, 15)
ll.display()  # 5 -> 10 -> 15 -> 20 -> None

ll.delete_node(15)
ll.display()  # 5 -> 10 -> 20 -> None
