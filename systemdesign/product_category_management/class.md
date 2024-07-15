+-----------------------------+
|      ICategoryComponent     |
+-----------------------------+
| + get_name()                |
| + add(component: ICategoryComponent)  |
| + remove(component: ICategoryComponent) |
| + move(component: ICategoryComponent, new_parent: ICategoryComponent) |
| + get_hierarchy()           |
+-----------------------------+
          ^
          |
+-----------------------------+
|          Category           |
+-----------------------------+
| - _name: str                |
| - _children: list           |
| - _parent: Category         |
| + get_name()                |
| + add(component: ICategoryComponent)  |
| + remove(component: ICategoryComponent) |
| + move(component: ICategoryComponent, new_parent: ICategoryComponent) |
| + get_hierarchy()           |
+-----------------------------+
