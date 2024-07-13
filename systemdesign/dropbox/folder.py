from systemdesign.dropbox.interface import IFileSystemComponent

class Folder(IFileSystemComponent):
    def __init__(self, name: str):
        self._name = name
        self._children = []
        self._parent = None

    def get_name(self) -> str:
        return self._name

    def add(self, component: 'IFileSystemComponent'):
        component._parent = self
        self._children.append(component)

    def remove(self, component: 'IFileSystemComponent'):
        self._children.remove(component)
        component._parent = None

    def move(self, new_parent: 'IFileSystemComponent'):
        if self._parent:
            self._parent.remove(self)
        new_parent.add(self)

    def get_path(self) -> str:
        path = []
        current = self
        while current:
            path.append(current.get_name())
            current = current._parent
        return '/'.join(reversed(path))
