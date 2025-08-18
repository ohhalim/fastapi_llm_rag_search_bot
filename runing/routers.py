from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas
from database import get_db
from repositories import UserRepository, ItemRepository
from services import UserService, ItemService

router = APIRouter(prefix="/users", tags =["users"])

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repository = UserRepository(db)
    return UserService(user_repository)

def get_item_service(db: Session = Depends(get_db)) -> ItemService:
    item_repository = ItemRepository(db)
    return ItemService(item_repository)

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
    return user_service.get_users(skip=skip, limit=limit)

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

@router.post("/items", response_model=schemas.Item)
def create_item(
    item: schemas.ItemCreate,
    item_service: ItemService = Depends(get_item_service)
):
    return item_service.create_item(item) 

@router.get("/items", response_model=List[schemas.Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    item_service: ItemService = Depends(get_item_service)
):
    return item_service.get_items(skip=skip, limit=limit)

@router.get("/items/{item_id}", response_model=schemas.Item)     
def read_item(
    item_id: int,
    item_service: ItemService = Depends(get_item_service)
):
    return item_service.get_item(item_id)

@router.put("/items/{item_id}", response_model=schemas.Item)
def update_item(
    item_id: int,  
    item_update: schemas.ItemUpdate,
    item_service: ItemService = Depends(get_item_service)
):
    return item_service.update_item(item_id, item_update)   

@router.delete("/items/{item_id}")
def delete_item(
    item_id: int,
    item_service: ItemService = Depends(get_item_service)   
):
    item_service.delete_item(item_id)
    return {"message":"Item deleted successfully"}