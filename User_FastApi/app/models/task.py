from sqlalchemy import Column, Integer, String, ForeignKey,Boolean, Enum as sqlenum
from app.core.database import Base
from sqlalchemy.orm import relationship
from enum import Enum

class TaskStatus(Enum):
    pending = "pending"
    completed = "completed"


class Task(Base):
    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("Users.user_id"))
    user = relationship("User", back_populates="tasks")
    is_deleted = Column(Boolean, default=False)
    status = Column(sqlenum(TaskStatus, name="task_status"),default=TaskStatus.pending, nullable=False)
