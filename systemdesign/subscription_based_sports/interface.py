from abc import ABC, abstractmethod

class IGameSubject(ABC):
    @abstractmethod
    def attach(self, subscriber):
        pass
    
    @abstractmethod
    def detach(self, subscriber):
        pass
    
    @abstractmethod
    def notify(self):
        pass

class ISubscriber(ABC):
    @abstractmethod
    def update(self, game):
        pass
