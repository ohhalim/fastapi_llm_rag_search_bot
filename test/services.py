from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .models import User
from .schemas import UserCreate
from .repositories import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: UserCreate):
    user_repo = UserRepository(db)
    hashed_password = pwd_context.hash(user.password)
    return user_repo.create_user(email=user.email, username=user.username, hashed_password=hashed_password)

def authenticate_user(db: Session, email: str, password: str):
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_email(email)
    if user and pwd_context.verify(password, user.hashed_password):
        return user
    return None