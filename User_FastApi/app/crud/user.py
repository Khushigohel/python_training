from sqlalchemy.orm import Session
from app.models.user import User
from app.schema.users import UserCreate
from app.utils.security import hash_password

def create_user(db:Session, user:UserCreate):
    db_users=User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(db_users)
    db.commit()
    db.refresh(db_users)
    return db_users
