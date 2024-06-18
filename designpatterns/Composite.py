'''
Composes objects into tree structures to represent part-whole hierarchies, allowing clients to treat individual objects and 
compositions uniformly.
'''
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return "Composite(" + "+".join(results) + ")"

leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
print(composite.operation())  # Output: Composite(Leaf+Leaf)
