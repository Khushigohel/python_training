from pydantic import BaseModel

class Taskcreate(BaseModel):
    title: str
    description: str | None = None

class Taskupdate(BaseModel):
    title: str
    description: str | None = None

class TaskResponse(BaseModel):
    id:int
    title:str
    description:str | None
    
    class Config:
        from_attributes = True