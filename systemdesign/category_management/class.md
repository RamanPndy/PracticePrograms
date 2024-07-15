+-----------------------------+
|      ICategoryComponent     |
+-----------------------------+
| + get_name()                |
| + add(component: ICategoryComponent)  |
| + remove(component: ICategoryComponent) |
| + display(indent: int)      |
+-----------------------------+
          ^
          |
+-----------------------------+
|          Category           |
+-----------------------------+
| - _name: str                |
| - _components: list         |
| + get_name()                |
| + add(component: ICategoryComponent)  |
| + remove(component: ICategoryComponent) |
| + display(indent: int)      |
+-----------------------------+
          ^
          |
+-----------------------------+
|          Product            |
+-----------------------------+
| - _name: str                |
| - _price: float             |
| + get_name()                |
| + add(component: ICategoryComponent)  |
| + remove(component: ICategoryComponent) |
| + display(indent: int)      |
+-----------------------------+
