from abc import ABC, abstractmethod
'''
Designing a product category tree in an e-commerce website involves structuring the hierarchy of product categories and subcategories. We can use Python along with design patterns and interfaces to create a flexible and scalable solution. Here's a basic low-level design using the composite design pattern and interfaces:

Interfaces:
CategoryInterface: Defines methods for managing categories.
ProductInterface: Defines methods for managing products.

Composite Pattern:
Category: Represents a category that can contain subcategories and/or products.

Product Class:
Product: Represents a product within a category.
'''

class CategoryInterface(ABC):
    @abstractmethod
    def add_category(self, category):
        pass
    
    @abstractmethod
    def remove_category(self, category):
        pass
    
    @abstractmethod
    def display(self):
        pass

class ProductInterface(ABC):
    @abstractmethod
    def add_product(self, product):
        pass
    
    @abstractmethod
    def remove_product(self, product):
        pass
    
    @abstractmethod
    def display(self):
        pass


class Category(CategoryInterface):
    def __init__(self, name):
        self.name = name
        self.subcategories = []
        self.products = []

    def add_category(self, category):
        self.subcategories.append(category)

    def remove_category(self, category):
        self.subcategories.remove(category)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def display(self):
        print(f"Category: {self.name}")
        print("Subcategories:")
        for subcategory in self.subcategories:
            subcategory.display()
        print("Products:")
        for product in self.products:
            product.display()


class Product(ProductInterface):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add_product(self, product):
        pass

    def remove_product(self, product):
        pass

    def display(self):
        print(f"Product: {self.name}, Price: ${self.price}")


# Creating categories and products
root_category = Category("Electronics")
mobiles_category = Category("Mobiles")
laptops_category = Category("Laptops")

iphone_product = Product("iPhone 13", 999)
samsung_product = Product("Samsung Galaxy S22", 899)
macbook_product = Product("MacBook Pro", 1499)

# Building the category tree
root_category.add_category(mobiles_category)
root_category.add_category(laptops_category)

mobiles_category.add_product(iphone_product)
mobiles_category.add_product(samsung_product)
laptops_category.add_product(macbook_product)

# Displaying the category tree
root_category.display()
