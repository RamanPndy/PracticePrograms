from systemdesign.product_category_management.interface import ICategoryComponent

class Category(ICategoryComponent):
    def __init__(self, name: str):
        self._name = name
        self._components = []

    def get_name(self) -> str:
        return self._name

    def add(self, component: 'ICategoryComponent'):
        self._components.append(component)

    def remove(self, component: 'ICategoryComponent'):
        self._components.remove(component)

    def display(self, indent: int = 0):
        print(' ' * indent + self._name)
        for component in self._components:
            component.display(indent + 2)

class Product(ICategoryComponent):
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_name(self) -> str:
        return self._name

    def add(self, component: 'ICategoryComponent'):
        raise NotImplementedError("Cannot add to a Product")

    def remove(self, component: 'ICategoryComponent'):
        raise NotImplementedError("Cannot remove from a Product")

    def display(self, indent: int = 0):
        print(' ' * indent + f'Product: {self._name}, Price: {self._price}')
