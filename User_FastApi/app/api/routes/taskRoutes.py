from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.crud.tasks import create_task,get_tasks,update_task,delete_task
from app.schema.task import Taskcreate,TaskResponse,Taskupdate
from app.core.database import SessionLocal
from app.api.deps import get_current_user_id
from app.api.auth import get_current_user
from app.models.user import User

router=APIRouter(prefix='/tasks',tags=["Tasks"])

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/add-task",response_model=TaskResponse)
def add_task(task:Taskcreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_task(db,task,current_user)

@router.get("/fetch-task",response_model=list[TaskResponse])
def get_all_task(db:Session = Depends(get_db)):
    return get_tasks(db)

@router.put("/update-task/{id}", response_model=TaskResponse)
def edit_task(task_id: int, task_update: Taskupdate, db: Session = Depends(get_db)):
    task = update_task(
        db, 
        task_id, 
        task_update
    )
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/delete-task/{id}")
def delete_tasks(id: int, db: Session = Depends(get_db)):
    task = delete_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}