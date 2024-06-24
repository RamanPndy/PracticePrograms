from designpatterns.SOLID.interface_seggregation.impl import HumanWorker, Robot
from designpatterns.SOLID.interface_seggregation.interface import Eatable, Sleepable, Workable

'''
The Interface Segregation Principle (ISP) is one of the SOLID principles of object-oriented design. 
It states that no client should be forced to depend on methods it does not use. In other words, it's better to have many small, 
specific interfaces than a single, large, general-purpose interface.

Explanation
Specific Interfaces: We created smaller, more specific interfaces (Workable, Eatable, Sleepable) instead of a single, 
large Worker interface.
Class Implementations: The Robot class only implements the Workable interface, avoiding unnecessary methods. 
The HumanWorker class implements all relevant interfaces (Workable, Eatable, Sleepable).
Client Usage: Functions like manage_worker and manage_human only depend on the methods they actually need.

By following the Interface Segregation Principle, we ensure that classes are not forced to implement methods they do not use, 
resulting in more modular, flexible, and maintainable code.
'''
def manage_worker(worker: Workable):
    worker.work()

def manage_human(human: Eatable, sleeper: Sleepable):
    human.eat()
    sleeper.sleep()

robot = Robot()
human_worker = HumanWorker()

manage_worker(robot)  # Only work method is needed
manage_worker(human_worker)  # Only work method is needed
manage_human(human_worker, human_worker)  # Only eat and sleep methods are needed
