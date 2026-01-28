from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.crud.user import create_user,get_users
from app.schema.users import UserCreate,UserResponse,LoginRequest
from app.core.database import SessionLocal
from app.models.user import User
from app.utils.security import verify_password
from app.core.jwt_handler import create_token
from fastapi.security import OAuth2PasswordRequestForm

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
def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = db.query(User).filter(
        User.name == form_data.username
    ).first()

    if not user or not verify_password(
        form_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    access_token = create_token(
        data={"user_id": user.user_id}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }