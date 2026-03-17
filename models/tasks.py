"""Task model definitions for the Taskflow application."""

import uuid
from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum


class Priority(Enum):
    """Enumeration for task priority levels."""

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


class Status(Enum):
    """Enumeration for task status states."""

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
    subtasks: list["Task"] = field(default_factory=list)

    def update_status(self, new_status: Status) -> None:
        """
        Update the status of the task.

        Args:
            new_status: The new status to set for this task.
        """
        self.status = new_status

    def is_overdue(self) -> bool:
        """
        Check if the task is past its end date.

        Returns:
            True if the task is overdue, False otherwise.
        """
        if self.end_date is None:
            return False
        return datetime.today().date() > self.end_date

    def __str__(self) -> str:
        """
        Return a string representation of the task.

        Returns:
            A formatted string showing priority, title, and status.
        """
        return f"[{self.priority.name}] {self.title} — {self.status.name}"


if __name__ == "__main__":
    pass



