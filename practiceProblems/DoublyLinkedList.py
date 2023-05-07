class Node:
    def __init__(self,data,n = None,p = None):
        self.data = data
        self.next = n
        self.previous = p

    def getNext(self):
        return self.next

    def setNext(self,n):
        self.next = n

    def getPrevious(self):
        return self.previous

    def setPrevious(self,p):
        self.previous = p

    def getData(self):
        return self.data

    def setData(self,d):
        self.data = d

class DLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def insert(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.head.setPrevious(node)
            self.head = node
            self.size += 1

    def insertAfter(self,prev,data):
        if prev is None:
            raise Exception
        node = Node(data)
        node.setNext(prev.next)
        prev.setNext(node)
        node.setPrevious(prev)
        if node.getNext() is not None:
            node.getNext().getPrevious(node)
        self.size += 1

    def find(self,data):
        if self.head is None:
            raise Exception
        if self.head.getData() == data:
            return self.head
        else:
            temp = self.head
            while temp is not None:
                if temp.getData() == data:
                    return temp
                temp = temp.getNext()

    def remove(self,data):
        if self.head is None:
            raise Exception

        node = self.find(data)
        prev = node.getPrevious()
        next = node.getNext()

        if next is not None and prev is not None:
            prev.setNext(next)
            next.setPrevious(prev)
            self.size -= 1
        elif next is not None and prev is None:
            self.head.setNext(next.getPrevious())
            self.head = next
            self.size -= 1
        elif next is None and prev is not None:
            prev.setNext(next)
            self.size -= 1

