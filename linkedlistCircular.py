class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        temp = self.head

        if temp is None:
            new_node = Node(data)
            new_node.next = temp
            self.head = new_node
        else:
            new_node = Node(data)
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            self.head = new_node

    def printList(self):
        temp = self.head

        if temp is None:
            raise Exception("There is no node in the Linked List")
        while(temp):
            print temp.data
            temp = temp.next
            if temp == self.head:
                break

if __name__ == "__main__":
    cl = CircularList()
    cl.insert(1)
    cl.printList()
    print '\n'
