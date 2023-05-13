class Array:
    def __init__(self) -> None:
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2

    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        for i in range(self.length):
            newArr[i] = self.arr[i]