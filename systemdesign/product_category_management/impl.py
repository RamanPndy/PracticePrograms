from systemdesign.product_category_management.category import Category

class ProductCategoryManager:
    def __init__(self, n: int):
        self._root = Category('ALL_PRODUCTS')
        self._categories = {'ALL_PRODUCTS': self._root}
        self._max_depth = n

    def add_product_category(self, category_name: str, parent_name: str = None):
        if category_name in self._categories:
            print(f"Category {category_name} already exists.")
            return

        parent = self._root if parent_name is None else self._categories.get(parent_name)
        if parent is None:
            print(f"Parent category {parent_name} does not exist.")
            return

        new_category = Category(category_name)
        parent.add(new_category)
        self._categories[category_name] = new_category

    def move_product_category(self, category_name: str, parent_name: str = None):
        category = self._categories.get(category_name)
        if category is None:
            print(f"Category {category_name} does not exist.")
            return

        new_parent = self._root if parent_name is None else self._categories.get(parent_name)
        if new_parent is None:
            print(f"Parent category {parent_name} does not exist.")
            return

        if category._parent:
            category._parent.move(category, new_parent)
        else:
            print(f"Category {category_name} is already under root category.")

    def get_product_category(self, category_name: str):
        category = self._categories.get(category_name)
        if category is None:
            print(f"Category {category_name} does not exist.")
            return
        print(category.get_hierarchy())