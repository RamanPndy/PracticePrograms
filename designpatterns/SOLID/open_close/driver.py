from designpatterns.SOLID.open_close.impl import Circle, Rectangle, Triangle

'''
The Open-Closed Principle (OCP) is one of the SOLID principles of object-oriented design. 
It states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. 
This means that the behavior of a module can be extended without modifying its source code.

Explanation
Abstraction: We created a Shape interface that declares the area method.
Concrete Implementations: We created separate classes (Rectangle, Circle, and Triangle) that inherit from the Shape interface 
and implement the area method.
Open for Extension: To add a new shape, such as a Triangle, we simply create a new class that implements the Shape interface.
Closed for Modification: The existing code for Rectangle and Circle does not need to be modified when adding a new shape.

By following the Open-Closed Principle, the design is more flexible and easier to extend with new functionality without 
modifying existing code, thus reducing the risk of introducing bugs.
'''
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(6, 8)
]

for shape in shapes:
    print(f"Area: {shape.area()}")
