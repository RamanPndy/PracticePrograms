class DQ:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return self.q == []

    def addFront(self,data):
        self.q.append(data)

    def addRear(self,data):
        self.q.insert(0,data)

    def removeFront(self):
        return self.q.pop()

    def removeRear(self):
        return self.q.pop(0)

    def getSize(self):
        return len(self.q)