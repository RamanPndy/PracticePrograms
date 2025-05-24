import random

class Node:
    '''
    A node in the skip list.
    Each node contains a key and a list of forward pointers.
    The number of forward pointers is determined by the level of the node.
    TC: O(1) for node creation
    SC: O(1) for storing node properties
    '''
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)  # List of forward pointers

class SkipList:
    '''
    A skip list is a data structure that allows for fast search, insertion, and deletion operations.
    It consists of multiple levels of linked lists, where each higher level skips over some elements
    of the lower level.
    The average time complexity for search, insert, and delete operations is O(log n).
    The space complexity is O(n) for storing n elements.
    '''
    MAX_LEVEL = 16  # Maximum level for this skip list
    P = 0.5         # Probability for random level generator

    def __init__(self):
        self.header = Node(-1, self.MAX_LEVEL)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.header

        # Move forward on each level to find the place to insert
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        # Insert only if key not present
        if current is None or current.key != key:
            lvl = self.random_level()

            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.header
                self.level = lvl

            new_node = Node(key, lvl)
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]

        if current and current.key == key:
            return True
        return False

    def delete(self, key):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.header

        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            # Decrease level if needed
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

    def display(self):
        print("Skip List:")
        for i in range(self.level + 1):
            current = self.header.forward[i]
            line = f"Level {i}: "
            while current:
                line += str(current.key) + " -> "
                current = current.forward[i]
            line += "None"
            print(line)

skiplist = SkipList()
skiplist.insert(3)
skiplist.insert(6)
skiplist.insert(7)
skiplist.insert(9)
skiplist.insert(12)
skiplist.insert(19)
skiplist.insert(17)

skiplist.display()

print("Search 9:", skiplist.search(9))  # True
print("Search 15:", skiplist.search(15))  # False

skiplist.delete(3)
print("After deleting 3:")
skiplist.display()
