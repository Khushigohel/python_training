from sqlalchemy.orm import Session
from app.models.task import Task
from app.schema.task import Taskcreate,Taskupdate

def create_task(db: Session, task_create: Taskcreate, user_id: int):
    task = Task(
        title=task_create.title,
        description=task_create.description,
        user_id=user_id,
        status=task_create.status 
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session):
    return db.query(Task).filter(Task.is_deleted == False).all()


def update_task(db: Session, id:int,task_update:Taskupdate):
    task=db.query(Task).filter(Task.id == id).first()
    
    if not task:
        return None
    if task_update.title:
        task.title = task_update.title
    if task_update.description:
        task.description=task_update.description
    if task_update.status:
        task.status=task_update.status
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, id: int):
    task = db.query(Task).filter(
        Task.id == id,
        Task.is_deleted == False
    ).first()

    if not task:
        return None

    task.is_deleted = True
    db.commit()
    db.refresh(task)

    return task

