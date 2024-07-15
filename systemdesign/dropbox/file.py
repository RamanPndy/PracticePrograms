from systemdesign.dropbox.interface import IFileSystemComponent

class File(IFileSystemComponent):
    def __init__(self, name: str):
        self._name = name
        self._parent = None

    def get_name(self) -> str:
        return self._name

    def add(self, component: 'IFileSystemComponent'):
        raise NotImplementedError("Cannot add to a File")

    def remove(self, component: 'IFileSystemComponent'):
        raise NotImplementedError("Cannot remove from a File")

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
