from datetime import datetime
from enum import Enum
from typing import List

class LogType(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    ERROR = "ERROR"
    WARNING = "WARNING"

class Log:
    def __init__(self, message: str, log_type: LogType, timestamp: datetime = datetime.now()):
        self.message = message
        self.log_type = log_type
        self.timestamp = timestamp

    def __repr__(self):
        return f"[{self.timestamp}] {self.log_type.name}: {self.message}"
