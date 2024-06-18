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

'''
Provides a simplified interface to a complex subsystem.
'''
class CPU:
    def freeze(self):
        return "CPU freeze"

    def jump(self, position):
        return f"CPU jump to {position}"

    def execute(self):
        return "CPU execute"

class Memory:
    def load(self, position, data):
        return f"Memory load {data} at {position}"

class HardDrive:
    def read(self, lba, size):
        return f"HardDrive read {size} bytes from {lba}"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        print(self.cpu.freeze())
        print(self.memory.load(0, "OS"))
        print(self.cpu.jump(0))
        print(self.cpu.execute())

computer = ComputerFacade()
computer.start()
