from dataclasses import dataclass 
from enum import Enum 
from datetime import datetime


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
    """Class for keeping track of the tasks in the taskflow."""
    title: str
    priority: Priority
    status: Status
    end_date: datetime = None
    father_task: 'Task' = None
    

if __name__ == "__main__":
    # Temp Ex
    task1 = Task("Taylor Swift", Priority.HIGH, Status.IN_PROGRESS, datetime(2026, 12, 13), None)