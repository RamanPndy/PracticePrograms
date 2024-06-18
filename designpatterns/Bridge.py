'''
In this example:
DrawingTool is the abstraction, which has a reference to the DrawingImplementor.
DrawingImplementor is the implementor interface that defines the methods for drawing shapes.
WindowsDrawingImplementor and LinuxDrawingImplementor are concrete implementors that implement the DrawingImplementor interface.
CircleTool and RectangleTool are refined abstractions that extend DrawingTool for specific shapes.
The Bridge pattern allows us to vary the implementor independently of the abstraction. 
In this case, we can draw circles and rectangles on different platforms (Windows and Linux) without changing the drawing tool classes.
'''
# Abstraction
class DrawingTool:
    def __init__(self, implementor):
        self.implementor = implementor

    def draw(self):
        pass

# Implementor Interface
class DrawingImplementor:
    def draw_circle(self, x, y, radius):
        pass

    def draw_rectangle(self, x1, y1, x2, y2):
        pass

# Concrete Implementor 1
class WindowsDrawingImplementor(DrawingImplementor):
    def draw_circle(self, x, y, radius):
        print(f"Drawing circle on Windows at ({x}, {y}) with radius {radius}")

    def draw_rectangle(self, x1, y1, x2, y2):
        print(f"Drawing rectangle on Windows from ({x1}, {y1}) to ({x2}, {y2})")

# Concrete Implementor 2
class LinuxDrawingImplementor(DrawingImplementor):
    def draw_circle(self, x, y, radius):
        print(f"Drawing circle on Linux at ({x}, {y}) with radius {radius}")

    def draw_rectangle(self, x1, y1, x2, y2):
        print(f"Drawing rectangle on Linux from ({x1}, {y1}) to ({x2}, {y2})")

# Refined Abstraction
class CircleTool(DrawingTool):
    def __init__(self, x, y, radius, implementor):
        super().__init__(implementor)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.implementor.draw_circle(self.x, self.y, self.radius)

# Refined Abstraction
class RectangleTool(DrawingTool):
    def __init__(self, x1, y1, x2, y2, implementor):
        super().__init__(implementor)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        self.implementor.draw_rectangle(self.x1, self.y1, self.x2, self.y2)

# Usage
windows_impl = WindowsDrawingImplementor()
linux_impl = LinuxDrawingImplementor()

circle_windows = CircleTool(10, 20, 5, windows_impl)
circle_windows.draw()

circle_linux = CircleTool(30, 40, 7, linux_impl)
circle_linux.draw()

rectangle_windows = RectangleTool(5, 5, 15, 15, windows_impl)
rectangle_windows.draw()

rectangle_linux = RectangleTool(10, 10, 20, 20, linux_impl)
rectangle_linux.draw()
