'''
Make fine grained interfaces that are client specific. Clients should not be forced to depend upon interfaces 
that they do not use. This principle deals with the disadvantages of implementing big interfaces.
interfaces should be as small as possible
'''

class Animal:
    def feed(self):
        pass

class Pet(Animal):
    def groom(self):
        pass

class Dog(Pet):
    def feed(self):
        pass
    def groom(self):
        pass

class Tiger(Animal):
    def feed(self):
        pass