+-----------------------------+
|    IFileSystemComponent     |
+-----------------------------+
| + get_name()                |
| + add(component: IFileSystemComponent)  |
| + remove(component: IFileSystemComponent) |
| + move(new_parent: IFileSystemComponent) |
| + get_path()                |
+-----------------------------+
          ^
          |
+-----------------------------+      +-----------------------------+
|           Folder            |      |            File             |
+-----------------------------+      +-----------------------------+
| - _name: str                |      | - _name: str                |
| - _children: list           |      | - _parent: IFileSystemComponent |
| - _parent: Folder           |      | + get_name()                |
| + get_name()                |      | + add(component: IFileSystemComponent)  |
| + add(component: IFileSystemComponent)  |      | + remove(component: IFileSystemComponent) |
| + remove(component: IFileSystemComponent) |      | + move(new_parent: IFileSystemComponent) |
| + move(new_parent: IFileSystemComponent) |      | + get_path()                |
| + get_path()                |      +-----------------------------+
+-----------------------------+
