class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None

    def insert(self,data):
        temp = self.head
        newNode = Node(data)
        newNode.next = self.head

        if temp is None:
            self.head = newNode
        else:
            while (temp.next != self.head):
                temp = temp.next