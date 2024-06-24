from designpatterns.SOLID.liskov_substituion.interface import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height

    def get_area(self):
        return self.side * self.side
