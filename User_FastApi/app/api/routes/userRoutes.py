from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.user import create_user
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