'''
In this example, Square inherits from Rectangle, but it overrides the set_width and set_height methods to ensure the width 
and height remain equal. This behavior breaks the Liskov Substitution Principle because Square does not behave like a 
Rectangle.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

def print_area(rectangle):
    rectangle.set_width(5)
    rectangle.set_height(10)
    print(f"Expected area: 50, Got: {rectangle.get_area()}")

rect = Rectangle(2, 3)
print_area(rect)

sq = Square(5)
print_area(sq)  # This will print an incorrect area because it violates LSP
