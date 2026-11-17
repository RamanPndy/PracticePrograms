from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class TaskStatus(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


@dataclass
class Task:
    id: UUID = None
    title: str
    description: str
    priority: Priority
    due_date: Optional[datetime] = None
    status: TaskStatus = TaskStatus.TODO
    created_at: datetime = None

    def __post_init__(self):
        if self.id is None:
            self.id = uuid4()

        if self.created_at is None:
            self.created_at = datetime.now()