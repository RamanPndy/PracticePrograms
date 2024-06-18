import copy

'''
Creates new objects by copying an existing object, known as the prototype.
'''
class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype1(Prototype):
    def __init__(self, field):
        self.field = field

prototype = ConcretePrototype1("value")
clone = prototype.clone()
print(clone.field)  # Output: value
