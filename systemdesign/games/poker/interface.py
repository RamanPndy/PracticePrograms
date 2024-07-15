from abc import ABC, abstractmethod

class IGameSubject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass

class IPlayerObserver(ABC):
    @abstractmethod
    def update(self, game):
        pass
