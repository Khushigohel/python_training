from app.core.database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
class User(Base):  
    __tablename__="Users"
    
    user_id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    tasks = relationship("Task", back_populates="user")
    