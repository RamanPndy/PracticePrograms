from designpatterns.SOLID.liskov_substituion.impl import Rectangle, Square

'''
The Liskov Substitution Principle (LSP) is one of the SOLID principles of object-oriented design. 
It states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of 
the program. 
In other words, subclasses should be able to substitute their base classes without the client knowing about the change.

Explanation
Abstraction: We created a Shape interface that declares the set_width, set_height, and get_area methods.
Rectangle and Square: Both Rectangle and Square inherit from Shape and implement the required methods in a way that preserves 
their unique behaviors.

By following the Liskov Substitution Principle, both Rectangle and Square can be used interchangeably wherever a Shape is 
expected without breaking the functionality or correctness of the program.
'''
def print_area(shape):
    shape.set_width(5)
    shape.set_height(10)
    print(f"Expected area: 50, Got: {shape.get_area()}")

rect = Rectangle(2, 3)
print_area(rect)  # This will work correctly

sq = Square(5)
print_area(sq)  # This will now work correctly as well
