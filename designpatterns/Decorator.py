'''
The Decorator pattern is a structural design pattern that allows behavior to be added to individual objects, either 
statically or dynamically, without affecting the behavior of other objects from the same class. 
It is often used to adhere to the Open/Closed Principle, which states that classes should be open for extension but closed 
for modification.

Allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the 
same class.

Example: Beverage Order System
'''

# Step 1: Create the base component
class Beverage:
    def cost(self):
        pass

class Coffee(Beverage):
    def cost(self):
        return 5  # Base cost of a coffee

# Step 2: Create the decorator base class
class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self._beverage = beverage
    
    def cost(self):
        return self._beverage.cost()
    
# Step 3: Create concrete decorators
class MilkDecorator(BeverageDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
    
    def cost(self):
        return self._beverage.cost() + 1  # Adding milk costs an extra $1

class SugarDecorator(BeverageDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
    
    def cost(self):
        return self._beverage.cost() + 0.5  # Adding sugar costs an extra $0.5

class WhippedCreamDecorator(BeverageDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
    
    def cost(self):
        return self._beverage.cost() + 1.5  # Adding whipped cream costs an extra $1.5

# Step 4: Use the decorators
# Create a plain coffee
beverage = Coffee()
print(f"Cost of plain coffee: ${beverage.cost()}")

# Add milk to the coffee
beverage_with_milk = MilkDecorator(beverage)
print(f"Cost of coffee with milk: ${beverage_with_milk.cost()}")

# Add sugar to the coffee with milk
beverage_with_milk_and_sugar = SugarDecorator(beverage_with_milk)
print(f"Cost of coffee with milk and sugar: ${beverage_with_milk_and_sugar.cost()}")

# Add whipped cream to the coffee with milk and sugar
beverage_with_all = WhippedCreamDecorator(beverage_with_milk_and_sugar)
print(f"Cost of coffee with milk, sugar, and whipped cream: ${beverage_with_all.cost()}")

'''
Explanation:
Base Component (Beverage): This defines the interface for objects that can have responsibilities added to them dynamically.
Concrete Component (Coffee): This is the class to which additional responsibilities can be attached.
Decorator Base Class (BeverageDecorator): This maintains a reference to a Beverage object and defines an interface that conforms to Beverage.
Concrete Decorators (MilkDecorator, SugarDecorator, WhippedCreamDecorator): These classes extend the functionality of the base beverage by adding extra cost.
The Decorator pattern provides a flexible alternative to subclassing for extending functionality. By using this pattern, you can combine various decorators in different ways to produce different behaviors.
'''
