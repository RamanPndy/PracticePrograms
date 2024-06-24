'''
Depend upon abstractions rather than concrete classes
'''

from abc import ABC, abstractmethod

class EventSender(ABC):
    @abstractmethod
    def send(self, event):
        pass

class Syslog(EventSender):
    def write(self, msg):
        with open('path', 'a') as f:
            f.write(msg)

    def send(self, event):
        self.write(event)

class EventStreamer:
    def __init__(self, sender: EventSender):
        self.event_stream = sender

    def send_event(self, event):
        self.event_stream.send(event)