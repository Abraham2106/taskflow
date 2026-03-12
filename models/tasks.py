from dataclasses import dataclass, field
from enum import Enum
from datetime import date, datetime
import uuid


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


class Status(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    DONE = 2


@dataclass
class Task:
    """Represents a task in the TaskFlow system."""

    title: str
    priority: Priority
    status: Status
    end_date: date | None = None
    father_id: str | None = None
    id: str = field(default_factory=lambda: uuid.uuid4().hex[:8])
    subtasks: list['Task'] = field(default_factory=list)

    def update_status(self, new_status: Status) -> None:
        """Updates the status of the task."""
        self.status = new_status

    def is_overdue(self) -> bool:
        """Returns True if the task is past its end_date."""
        if self.end_date is None:
            return False
        return datetime.today().date() > self.end_date
    
    def __str__(self) -> str:
        return f"[{self.priority.name}] {self.title} — {self.status.name}"

if __name__ == "__main__":
    pass 


