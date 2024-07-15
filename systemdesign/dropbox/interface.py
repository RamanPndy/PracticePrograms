from abc import ABC, abstractmethod

class IFileSystemComponent(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def add(self, component: 'IFileSystemComponent'):
        pass

    @abstractmethod
    def remove(self, component: 'IFileSystemComponent'):
        pass

    @abstractmethod
    def move(self, new_parent: 'IFileSystemComponent'):
        pass

    @abstractmethod
    def get_path(self) -> str:
        pass
