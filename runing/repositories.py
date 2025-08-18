from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas

class UserRepository:
    def __init__(self, db: Session):
        self.db = db 
        
    def get_user(self, user_id: int) -> Optional[models.User]:
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def get_user_by_email(self, email:str) -> Optional[models.User]:
        return self.db.query(models.User).filter(models.User.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100) -> List[models.User]:
        return self.db.query(models.User).offset(skip).limit(limit).all()
    
    def create_user(self, user: schemas.UserCreate) -> models.User:
        db_user = models.User(**user.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int,user_update: schemas.UserUpdate) -> Optional[models.User]:
        db_user = self.get_user(user_id)
        if db_user:
            update_data = user_update.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_user, field, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user



    def delete_user(self, user_id: int) -> bool:
        db_user = self.get_user(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return True
        return False


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_item(self, item_id: int) -> Optional[models.Item]:
        return self.db.query(models.Item).filter(models.Item.id == item_id).first()
    
    def get_items(self, skip: int = 0, limit: int = 100) -> List[models.Item]:
        return self.db.query(models.Item).offset(skip).limit(limit).all()
    
    def create_item(self, item: schemas.ItemCreate) -> models.Item:
        db_item = models.Item(**item.model_dump())
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
    
    def update_item(self, item_id: int, item_update: schemas.ItemUpdate) -> Optional[models.Item]:
        db_item = self.get_item(item_id)
        if db_item:
            update_data = item_update.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_item, field, value)
            self.db.commit()
            self.db.refresh(db_item)
        return db_item
    
    def delete_item(self, item_id: int) -> bool: 
        db_item = self.get_item(item_id)
        if db_item:
            self.db.delete(db_item)
            self.db.commit()
            return True
        return False