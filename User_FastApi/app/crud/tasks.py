from sqlalchemy.orm import Session
from app.models.task import Task

def create_task(db: Session, title: str, description: str, user_id: int):
    task = Task(title=title, description=description, user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session):
    return db.query(Task).filter(Task.is_deleted == False).all()


def update_task(db: Session, id:int,title:str, description: str):
    task=db.query(Task).filter(Task.id == id).first()
    
    if not task:
        return None
    if title:
        task.title = title
    if description:
        task.description=description
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

