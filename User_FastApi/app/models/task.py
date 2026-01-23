from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from app.core.database import Base
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("Users.user_id"))
    user = relationship("User", back_populates="tasks")
    is_deleted = Column(Boolean, default=False)
