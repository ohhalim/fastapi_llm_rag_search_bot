from typing import List, Optional
from fastapi import HTTPException
import schemas
from repositories import UserRepository, ItemRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: schemas.UserCreate) -> schemas.User:

        db_user = self.user_repository.get_user_by_email(user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        created_user = self.user_repository.create_user(user)
        return schemas.User.model_validate(created_user)

    def get_user(self, user_id: int) -> schemas.User:
        db_user = self.user_repository.get_user(user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        return schemas.User.model_validate(db_user)

    def get_users(self, skip: int = 0, limit: int = 100) -> List[schemas.User]:
        users = self.user_repository.get_users(skip=skip,limit=limit)
        return [schemas.User.model_validate(user) for user in users]

    def update_user(self, user_id: int, user_update: schemas.UserUpdate) -> schemas.User:
        update_user = self.user_repository.update_user(user_id, user_update)
        if not update_user:
            raise HTTPException(status_code=404, detail="User not found")
        return schemas.User.model_validate(update_user)

    def delete_user(self, user_id: int) -> bool:
        deleted = self.user_repository.delete_user(user_id)
        if not deleted:
            raise HTTPException(status_code = 404, detail="User not found")
        return True


class ItemService:  
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def create_item(self, item: schemas.ItemCreate) -> schemas.Item:
        created_item = self.item_repository.create_item(item)
        return schemas.Item.model_validate(created_item)
    
    def get_item(self, item_id: int) -> schemas.Item:
        db_item = self.item_repository.get_item(item_id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return schemas.Item.model_validate(db_item)
    
    def get_items(self, skip: int = 0, limit: int = 100) -> List[schemas.Item]:
        items = self.item_repository.get_items(skip=skip, limit=limit)
        return [schemas.Item.model_validate(item) for item in items]
    
    def update_item(self, item_id: int, item_update: schemas.ItemUpdate) -> schemas.Item:
        updated_item = self.item_repository.update_item(item_id, item_update)
        if not updated_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return schemas.Item.model_validate(updated_item)
    
    def delete_item(self, item_id: int) -> bool:
        deleted = self.item_repository.delete_item(item_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Item not found")