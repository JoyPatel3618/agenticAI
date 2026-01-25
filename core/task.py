import uuid
from enum import Enum

class TaskState(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Task:
    """A task is a unit of work with metadata
     - Agents come and go,
       Tasks stay and evolve"""
    def __init__(self, description, context=None):
        self.id = uuid.uuid4()
        self.state = TaskState.PENDING
        self.description=description
        self.context = context if context is not None else {}
    
    def __repr__(self):
        return f"Task(id={self.id}, state={self.state.value}, description={self.description})"

