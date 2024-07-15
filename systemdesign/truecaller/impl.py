from typing import List
from systemdesign.truecaller.interface import ICallerIDService, ISubscriber
from systemdesign.truecaller.models import CallerInfo

class CallerIDService(ICallerIDService):
    def __init__(self):
        self.subscribers: List[ISubscriber] = []

    def identifyCaller(self, phoneNumber: str):
        # Implementation of caller identification
        info = CallerInfo(phoneNumber, "John Doe", 4)
        self.notifySubscribers(info)
        return info

    def subscribe(self, subscriber: ISubscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: ISubscriber):
        self.subscribers.remove(subscriber)

    def notifySubscribers(self, info: CallerInfo):
        for subscriber in self.subscribers:
            subscriber.update(info)

class CallLogger(ISubscriber):
    def update(self, info: CallerInfo):
        # Log the call information
        print(f"Logging call from {info.name}")

class CallBlocker(ISubscriber):
    def update(self, info: CallerInfo):
        # Block the call if it is spam
        print(f"Blocking call from {info.name} if spam score is high")