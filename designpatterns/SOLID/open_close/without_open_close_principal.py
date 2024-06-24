'''
If we want to add support for new shapes, such as triangles, we need to modify the Shape class, violating the Open-Closed Principle.
'''
class Shape:
    def __init__(self, type, width=0, height=0, radius=0):
        self.type = type
        self.width = width
        self.height = height
        self.radius = radius

    def area(self):
        if self.type == 'rectangle':
            return self.width * self.height
        elif self.type == 'circle':
            return 3.14 * self.radius * self.radius

shapes = [
    Shape('rectangle', width=5, height=10),
    Shape('circle', radius=7)
]

for shape in shapes:
    print(f"Area: {shape.area()}")
