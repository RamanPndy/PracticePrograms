class YoutubeChannel:
    def __init__(self, name) -> None:
        self.name = name
        self.subscribers = []
    
    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)

from abc import ABC, abstractmethod

class YoutubeSubscriber(ABC):

    @abstractmethod
    def sendNotification(self, event):
        pass

class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name) -> None:
        self.name = name

    def sendNotification(self, channel, event):
        super().sendNotification(event)
        print ("User {self.name} reciveed notification from {channel}: {event}")
    
channel = YoutubeChannel("neetcode")
channel.subscribe("raman")
channel.subscribe("siddharth")
channel.subscribe("pankaj")

channel.notify("new video released")

'''
Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and 
updated automatically.
'''
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        pass

class ConcreteObserver(Observer):
    def update(self):
        print("Observer notified!")

# Usage
subject = Subject()
observer = ConcreteObserver()
subject.attach(observer)
subject.notify()  # Observer notified!
