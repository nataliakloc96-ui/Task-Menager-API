from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from enum import Enum

class TaskBase(BaseModel):
    title: str
    done: bool = False

class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent" 

class TaskCreate(BaseModel):
    title: str
    due_date: datetime | None = None
    priority: TaskPriority = TaskPriority.medium


class TaskOut(BaseModel):
    id: int
    title: str
    status: str

    class Config:
        from_attributes = True

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"



class TaskUpdate(BaseModel):
    title: str | None = None
    status: TaskStatus | None = None
    priority: TaskPriority | None = None
    due_date: datetime | None = None


