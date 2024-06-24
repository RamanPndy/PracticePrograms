from designpatterns.SOLID.interface_seggregation.interface import Eatable, Sleepable, Workable

class Robot(Workable):
    def work(self):
        print("Robot working...")

class HumanWorker(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working...")

    def eat(self):
        print("Human eating...")

    def sleep(self):
        print("Human sleeping...")
