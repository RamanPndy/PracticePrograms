from systemdesign.product_category_management.interface import ICategoryComponent

class Category(ICategoryComponent):
    def __init__(self, name: str):
        self._name = name
        self._children = []
        self._parent = None

    def get_name(self) -> str:
        return self._name

    def add(self, component: 'ICategoryComponent'):
        component._parent = self
        self._children.append(component)

    def remove(self, component: 'ICategoryComponent'):
        self._children.remove(component)
        component._parent = None

    def move(self, component: 'ICategoryComponent', new_parent: 'ICategoryComponent'):
        if component in self._children:
            self.remove(component)
            new_parent.add(component)

    def get_hierarchy(self) -> str:
        hierarchy = []
        current = self
        while current:
            hierarchy.append(current.get_name())
            current = current._parent
        return ' > '.join(reversed(hierarchy))
