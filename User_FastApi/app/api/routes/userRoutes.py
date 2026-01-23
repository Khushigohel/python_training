from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.user import create_user,get_users
from app.schema.users import UserCreate,UserResponse
from app.core.database import SessionLocal

router=APIRouter(prefix="/users",tags=["Users"])

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/",response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return get_users(db)