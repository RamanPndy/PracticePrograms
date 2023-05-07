class Stack:
    def __init__(self):
        self.l = []

    def push(self,data):
        self.l.append(data)

    def popS(self):
        if self.size() == 0:
            raise Exception("There is no item in the stack")
        return self.l.pop()

    def size(self):
        return len(self.l)

    def peek(self):
        return self.l[self.size()-1]

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    print s.size()
    print s.popS()
    print s.peek()