from systemdesign.doc_management.DropBox import Folder, File

class FileSystemManager:
    def __init__(self):
        self._root = Folder('ROOT')
        self._items = {'ROOT': self._root}

    def add_file(self, file_name: str, parent_folder_name: str):
        if file_name in self._items:
            print(f"File {file_name} already exists.")
            return

        parent = self._items.get(parent_folder_name)
        if parent is None or not isinstance(parent, Folder):
            print(f"Parent folder {parent_folder_name} does not exist or is not a folder.")
            return

        new_file = File(file_name)
        parent.add(new_file)
        self._items[file_name] = new_file

    def add_folder(self, folder_name: str, parent_folder_name: str):
        if folder_name in self._items:
            print(f"Folder {folder_name} already exists.")
            return

        parent = self._items.get(parent_folder_name)
        if parent is None or not isinstance(parent, Folder):
            print(f"Parent folder {parent_folder_name} does not exist or is not a folder.")
            return

        new_folder = Folder(folder_name)
        parent.add(new_folder)
        self._items[folder_name] = new_folder

    def move_item(self, item_name: str, new_parent_folder_name: str):
        item = self._items.get(item_name)
        if item is None:
            print(f"Item {item_name} does not exist.")
            return

        new_parent = self._items.get(new_parent_folder_name)
        if new_parent is None or not isinstance(new_parent, Folder):
            print(f"New parent folder {new_parent_folder_name} does not exist or is not a folder.")
            return

        item.move(new_parent)

    def get_item(self, item_name: str):
        item = self._items.get(item_name)
        if item is None:
            print(f"Item {item_name} does not exist.")
            return
        print(item.get_path())