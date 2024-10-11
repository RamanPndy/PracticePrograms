from typing import List
from systemdesign.log_tracking_system.interface import ILogFilterStrategy, ILogSearchStrategy, IObserver, ISubject
from systemdesign.log_tracking_system.models import Log

class LogTrackerService(ISubject):
    def __init__(self):
        self.observers: List[IObserver] = []
        self.logs: List[Log] = []

    def register_observer(self, observer: IObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: IObserver):
        self.observers.remove(observer)

    def notify_observers(self, log: Log):
        for observer in self.observers:
            observer.update(log)

    def add_log(self, log: Log):
        self.logs.append(log)
        self.notify_observers(log)

    def get_logs(self) -> List[Log]:
        return self.logs

class LogFilterService:
    def __init__(self, strategy: ILogFilterStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ILogFilterStrategy):
        self.strategy = strategy

    def filter_logs(self, logs: List[Log]) -> List[Log]:
        return self.strategy.filter(logs)

class LogSearchService:
    def __init__(self, strategy: ILogSearchStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ILogSearchStrategy):
        self.strategy = strategy

    def search_logs(self, logs: List[Log], query: str) -> List[Log]:
        return self.strategy.search(logs, query)
