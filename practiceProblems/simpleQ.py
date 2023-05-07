class Queue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.q = [None] * self.size
        self.length = 0

    def isEmpty(self):
        if ((self.front == -1) and (self.rear == -1)):
            return True
        else:
            return False

    def isFull(self):
        if ((self.front == 0) and (self.rear == self.size - 1)):
            return True
        else:
            return False

    def getSize(self):
        return self.length

    def enqueue(self, data):
        if (self.isFull()):
            raise Exception("Overflow")
        elif (self.getSize() >= 1):
            self.rear += 1
            self.q[self.rear] = data
            self.length += 1
        else:
            self.rear += 1
            self.front += 1
            self.q[self.rear] = data
            self.length += 1

    def dequeue(self):
        if (self.isEmpty()):
            raise Exception("Underflow")
        elif (self.front == self.rear):
            t = self.q[self.front]
            self.rear -= 1
            self.front -= 1
            self.length = 0
            return t
        else:
            self.front += 1
            self.length -= 1
            return self.q[self.front]

    def peek(self):
        return self.q[self.front]

    def printQ(self):
        if (self.isEmpty()):
            raise Exception("No Such Element")
        else:
            for i in range(self.length):
                print self.q[i]


if __name__ == "__main__":
    q = Queue(5)
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    q.enqueue("d")
    # print q.length
    # print q.getSize()
    print q.printQ()
