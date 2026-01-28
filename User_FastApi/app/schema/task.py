from pydantic import BaseModel
from enum import Enum

class TaskStatus(str,Enum):
    pending = "pending"
    completed = "completed"
    progress = "progress"
    todo="todo"

class Taskcreate(BaseModel):
    title: str
    description: str | None = None

class Taskupdate(BaseModel):
    title: str
    description: str | None = None
    status : TaskStatus
    

class TaskResponse(BaseModel):
    id:int
    title:str
    description:str | None
    status : TaskStatus
    
    class Config:
        from_attributes = True