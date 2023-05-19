import sys

class ProductCategory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def move_to(self, new_parent):
        if self.parent:
            self.parent.children.remove(self)
        new_parent.add_child(self)
        self.parent = new_parent

    def get_category_hierarchy(self):
        hierarchy = [self.name]
        current = self.parent
        while current:
            hierarchy.insert(0, current.name)
            current = current.parent
        return hierarchy

    def find_category(self, name):
        if self.name == name:
            return self
        for child in self.children:
            found_category = child.find_category(name)
            if found_category:
                return found_category
        return None


class CatalogManager:
    def __init__(self, n_level):
        self.n_level = n_level
        self.root_category = ProductCategory('ALL PRODUCTS')

    def add_product_category(self, product_category_name, parent_product_category_name):
        if self.n_level > 1 and parent_product_category_name is None:
            print("Error: Parent product category name is required.")
            return
        parent_category = self.root_category if parent_product_category_name is None else self.root_category.find_category(parent_product_category_name)
        if parent_category is None:
            print("Error: Parent product category does not exist.")
            return
        if product_category_name in [category.name for category in parent_category.children]:
            print("Error: Product category with the same name already exists.")
            return
        new_category = ProductCategory(product_category_name, parent_category)
        parent_category.add_child(new_category)
        print(f"Product category '{product_category_name}' added.")

    def move_product_category(self, product_category_name, parent_product_category_name):
        if self.n_level > 1 and parent_product_category_name is None:
            print("Error: Parent product category name is required.")
            return
        category = self.root_category.find_category(product_category_name)
        if category is None:
            print(f"Error: Product category '{product_category_name}' does not exist.")
            return
        if parent_product_category_name is None:
            new_parent_category = self.root_category
        else:
            new_parent_category = self.root_category.find_category(parent_product_category_name)
        if new_parent_category is None:
            print(f"Error: Parent product category '{parent_product_category_name}' does not exist.")
            return
        if category.parent == new_parent_category:
            print("Error: Product category is already under the specified parent category.")
            return
        category.move_to(new_parent_category)
        print(f"Product category '{product_category_name}' moved.")

    def get_product_category(self, product_category_name):
        category = self.root_category.find_category(product_category_name)
        if category is None:
            print(f"Error: Product category '{product_category_name}' does not exist.")
        else:
            hierarchy = category.get_category_hierarchy()
            print("Category Hierarchy:")
            for level, category_name in enumerate(hierarchy):
                indent = '  ' * level
                print(f"{indent}{category_name}")


def parse_command_line_arguments():
    if len(sys.argv) < 2:
        print("Error: Please provide the number of hierarchy levels as a program argument.")
        return None
    try:
        n_level = int(sys.argv[1])
        if n_level < 2 or n_level >= 10:
            print("Error: The number of hierarchy levels must be between 2 and 9.")
            return None
        return n_level
    except ValueError:
        print("Error: Invalid number of hierarchy levels specified.")
        return None


def main():
    n_level = parse_command_line_arguments()
    if n_level is None:
        return
    catalog_manager = CatalogManager(n_level)

    while True:
        command = input("Enter a command (ADD_PRODUCT_CATEGORY, MOVE_PRODUCT_CATEGORY, GET_PRODUCT_CATEGORY, EXIT): ")
        if command == "ADD_PRODUCT_CATEGORY":
            product_category_name = input("Enter the product category name: ")
            parent_product_category_name = input("Enter the parent product category name (leave blank for root category): ")
            catalog_manager.add_product_category(product_category_name, parent_product_category_name)
        elif command == "MOVE_PRODUCT_CATEGORY":
            product_category_name = input("Enter the product category name: ")
            parent_product_category_name = input("Enter the new parent product category name (leave blank for root category): ")
            catalog_manager.move_product_category(product_category_name, parent_product_category_name)
        elif command == "GET_PRODUCT_CATEGORY":
            product_category_name = input("Enter the product category name: ")
            catalog_manager.get_product_category(product_category_name)
        elif command == "EXIT":
            break
        else:
            print("Error: Invalid command.")

if __name__ == '__main__':
    main()
