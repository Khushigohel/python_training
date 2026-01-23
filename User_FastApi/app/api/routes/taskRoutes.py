from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.tasks import create_task,get_tasks
from app.schema.task import Taskcreate,TaskResponse,Taskupdate
from app.core.database import SessionLocal
from app.api.deps import get_current_user_id

router=APIRouter(prefix='/tasks',tags=["Tasks"])

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/",response_model=TaskResponse)
def add_task(task:Taskcreate,user_id:int =  Depends(get_current_user_id), db: Session = Depends(get_db)):
    return create_task(db,task.title,task.description,user_id)

@router.get("/",response_model=list[TaskResponse])
def get_all_task(db:Session = Depends(get_db)):
    return get_tasks(db)

