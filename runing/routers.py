from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas
from database import get_db
from repositories import UserRepository
from services import UserService

router = APIRouter(prefix="/users", tags =["users"])

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repository = UserRepository(db)
    return UserService(user_repository)

@router.post("/", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    return user_service.create_user(user)

@router.get("/", response_model=List[schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    user_service: UserService = Depends(get_user_service)
):
    return user_service.get_user(skip=skip, limit=limit)

@router.get("/{user_id}", response_model=schemas.User)
def read_user(
    user_id: int, 
    user_service: UserService = Depends(get_user_service)
):
    return user_service.get_user(user_id)

@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int,
    user_update: schemas.UserUpdate,
    user_service: UserService = Depends(get_user_service)
):
    return user_service.update_user(user_id, user_update)

@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    user_service.delete_user(user_id)
    return {"message":"User deleted successfully"}
