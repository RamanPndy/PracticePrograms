class Q:
    def __init__(self):
        self.l = []

    def getSize(self):
        return len(self.l)

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

    def enqueue(self,data):
        self.l.append(data)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Underflow")
        else:
            return self.l.pop(0)

class StackUQ:
    def __init__(self):
        self.q1 = Q()
        self.q2 = Q()
        self.size = 0

    def push(self,data):
        self.q1.enqueue(data)
        self.size += 1

    def getSize(self):
        return self.size

    def pop(self):
        if self.getSize() == 0:
            raise Exception("Stack is Empty")
        else:
            for i in range(self.q1.getSize()-1):
                self.q2.enqueue(self.q1.dequeue())
            d = self.q1.dequeue()
            self.q1,self.q2 = self.q2,self.q1
            self.size -= 1
            return d

q = Q()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print q.l
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()


