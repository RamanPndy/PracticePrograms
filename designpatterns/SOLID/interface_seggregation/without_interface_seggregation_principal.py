'''
In this example, the Robot class is forced to implement methods eat and sleep even though it doesn't need them, 
which violates ISP.
'''
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

class Robot(Worker):
    def work(self):
        print("Robot working...")

    def eat(self):
        pass  # Robots don't eat

    def sleep(self):
        pass  # Robots don't sleep

class HumanWorker(Worker):
    def work(self):
        print("Human working...")

    def eat(self):
        print("Human eating...")

    def sleep(self):
        print("Human sleeping...")
