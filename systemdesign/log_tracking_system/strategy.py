from datetime import datetime
from typing import List

from systemdesign.log_tracking_system.interface import ILogFilterStrategy, ILogSearchStrategy
from systemdesign.log_tracking_system.models import Log, LogType

class LogTypeFilterStrategy(ILogFilterStrategy):
    def __init__(self, log_type: LogType):
        self.log_type = log_type

    def filter(self, logs: List[Log]) -> List[Log]:
        return [log for log in logs if log.log_type == self.log_type]

class TimeRangeFilterStrategy(ILogFilterStrategy):
    def __init__(self, start_time: datetime, end_time: datetime):
        self.start_time = start_time
        self.end_time = end_time

    def filter(self, logs: List[Log]) -> List[Log]:
        return [log for log in logs if self.start_time <= log.timestamp <= self.end_time]

class LogMessageSearchStrategy(ILogSearchStrategy):
    def search(self, logs: List[Log], query: str) -> List[Log]:
        return [log for log in logs if query in log.message]

