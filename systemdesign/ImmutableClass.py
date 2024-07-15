'''
Steps to Design an Immutable Class
Use the Constructor for Initialization: Set all attributes during the initialization of the object.
Prevent Modification: Ensure attributes cannot be modified after they are set. This can be done by:
Not providing any setter methods.
Using private attributes and not exposing any methods to modify them.
Ensure Immutability for All Attributes: If the class contains mutable objects (e.g., lists or dictionaries), ensure these cannot be modified after creation.
Override __setattr__ and __delattr__ Methods: Prevent attributes from being modified or deleted after the object is created.

Key Points
Initialization: The __init__ method sets the attributes using super().__setattr__() to avoid calling the overridden __setattr__ method.
Prevent Modification: The __setattr__ method is overridden to raise an AttributeError if an attempt is made to modify any attribute.
Prevent Deletion: The __delattr__ method is overridden to raise an AttributeError if an attempt is made to delete any attribute.
Getter Methods: Provide getter methods to access the private attributes.
'''
class ImmutableCar:
    def __init__(self, make: str, model: str, year: int):
        super().__setattr__('_make', make)
        super().__setattr__('_model', model)
        super().__setattr__('_year', year)

    def __setattr__(self, key, value):
        raise AttributeError(f"Cannot modify attribute '{key}' of an immutable instance")

    def __delattr__(self, key):
        raise AttributeError(f"Cannot delete attribute '{key}' of an immutable instance")

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def __repr__(self):
        return f"ImmutableCar(make='{self._make}', model='{self._model}', year={self._year})"

# Example usage
car = ImmutableCar(make="Toyota", model="Corolla", year=2020)
print(car)

# Access attributes using getter methods
print(car.get_make())  # Output: Toyota
print(car.get_model())  # Output: Corolla
print(car.get_year())  # Output: 2020

# Trying to modify or delete an attribute will raise an AttributeError
try:
    car._make = "Honda"
except AttributeError as e:
    print(e)  # Output: Cannot modify attribute '_make' of an immutable instance

try:
    del car._make
except AttributeError as e:
    print(e)  # Output: Cannot delete attribute '_make' of an immutable instance
