from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import schemas, services
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# 
@router.post("/create/", response_model=schemas.UserResponse)
def user_create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db=db, user=user)

@router.post("/login/")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = services.authenticate_user(db=db, email=email, password=password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="이메일 또는 비밀번호가 올바르지 않습니다.")
    return {"message": f"{user.username}님, 반갑습니다!"}