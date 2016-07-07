class Node:
    def __init__(self,data = None,nextNode = None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNode(self):
        return self.nextNode

    def setNextNode(self,newNode=None):
        self.nextNode = newNode

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head

    def insert(self,data):
        new_node = Node(data)
        new_node.setNextNode(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNode()
        return  count

    def search(self,data):
        current = self.head
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNode()

        if current == None:
            print "There is no such item!!!"
