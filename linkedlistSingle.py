class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        temp = self.head
        prev = None
        if temp is None:
            node = Node(data)
            node.next = temp
            self.head = node
        else:
            while(temp is not None):
                prev = temp
                temp = temp.next
            node = Node(data)
            prev.next = node

    def insertAtPos(self,pos,data):
        temp = self.head
        prev = None
        l = 0
        while l < pos:
            l += 1
            prev = temp
            temp = temp.next
        node = Node(data)
        prev.next = node
        node.next = temp

    def getNodeAtPos(self,pos):
        temp = self.head
        l = 0
        if temp is None:
            raise Exception("There is no node in the linked list")
        if pos > self.length():
            raise Exception("Overflow Condition")
        while l != pos-1:
            l += 1
            temp = temp.next

        print temp.data
        return temp

    def getPosOfNode(self,data):
        temp = self.head
        if temp is None:
            raise Exception("There is no node in the linked list")
        l = 0
        while temp.data != data:
            l += 1
            temp = temp.next

        print l+1
        return l+1

    def printList(self):
        temp = self.head
        if temp is None:
            raise Exception("No node in linked list")
        while temp is not None:
            print temp.data,
            temp = temp.next

    def remove(self,data):
        temp = self.head
        prev = None
        next_node = temp.next
        if temp is None:
            raise  Exception("No node in linked list")
        if (temp.data == data) and (next_node is not None):
            temp = next_node
            self.head = temp
            return
        while(temp.data !=data and temp != None):
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def removeAtPos(self,pos):
        temp = self.head
        prev = None
        next_node = temp.next
        l = 0
        if temp is None:
            raise Exception("There is no node in linked list")
        if pos > self.length():
            raise Exception("Overflow Condition")
        if l == pos-1:
            temp = next_node
            self.head = temp
            return
        while l != pos-1:
            l += 1
            if temp is None:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def length(self):
        temp = self.head
        l = 0
        while temp is not None:
            l += 1
            temp = temp.next
        return l

    def reverse(self):
        temp = self.head
        prev = None
        next_node = None

        if temp is None:
            raise Exception("There is no node in the linked list")
        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

if __name__=="__main__":
    sl = SingleList()
    sl.insert(1)
    sl.insert(2)
    sl.insert(3)
    sl.insert(4)
    sl.insert(5)
    sl.insertAtPos(3,6)
    sl.insertAtPos(6,7)
    sl.insertAtPos(4,8)
    sl.insert(9)
    sl.printList()
    print '\n'
    sl.reverse()
    sl.printList()
    # sl.removeAtPos(2)
    # sl.removeAtPos(8)
    # sl.removeAtPos(1)
    # sl.printList()
    # print '\n'
    # sl.getNodeAtPos(4)
    # print '\n'
    # sl.getPosOfNode(8)
    # print '\n'
    # sl.reverse()

