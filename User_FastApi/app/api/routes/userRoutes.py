from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.crud.user import create_user,get_users
from app.schema.users import UserCreate,UserResponse,LoginRequest
from app.core.database import SessionLocal
from app.models.user import User
from app.utils.security import verify_password
from app.core.jwt_handler import create_token

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

@router.get("/getUser",response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/login")
def login(data : LoginRequest, db: Session = Depends(get_db)):
    user= db.query(User).filter(User.name == data.username).first()
    
    if not user or not verify_password(data.password , user.password):
        raise HTTPException(status_code=404 , detail= "Username and password invalid Try Again Later...")
    
    token = create_token({"user_id" : user.user_id})
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }