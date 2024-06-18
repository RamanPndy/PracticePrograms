class Burger:
    def __init__(self, ingrediants) -> None:
        self.ingrediants = ingrediants

class BurgerFactory:
    def createCheeseBurger(self):
        ingrediants = ["bun", "cheese"]
        return Burger(ingrediants)
    
    def createDeluxCheeseBurger(self):
        ingrediants = ["bun", "cheese", "tomato", "lettuce"]
        return Burger(ingrediants)
    
    def createVeganBurger(self):
        ingrediants = ["bun", "sauce", "veggie-patty"]
        return Burger(ingrediants)
    
burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger()
burgerFactory.createVeganBurger()

'''
Defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
'''
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            return None

# Usage
factory = AnimalFactory()
dog = factory.create_animal('dog')
cat = factory.create_animal('cat')
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
