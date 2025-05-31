from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas

class UserRepository:
    def __init__(self, db: Session):
        self.db = db 
        
    def get_user(self, user_id: int) -> Optional[models.User]:
        return self.db.query(models.User).filter(models.User.id == id).first()

    def get_user_by_email(self, email:str) -> Optional[models.User]:
        return self.db.query(models.User).filter(models.User.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100) -> List[models.User]:
        return self.dbquery(models.User).offset(skip).limit(limit).all()
    
    def create_user(self, user: schemas.UserCreate) -> models.User:
        db_user = models.User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int,user_update: schemas.UserUpdate) -> Optional[models.User]:
        db_user = self.get_user(user_id)
        if db_user:
            update_data = user_update.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_user, field, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(slef, user_id: int) -> bool:
        db_user = self.get_user(user_id)
        if db_user:
            update_data = user_update.dict(exclude_unset=True)
            for field. value in update_data.items():
                setattr(db_user, field, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(delf, user_id: int) -> bool:
        db_user = self.get_user(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        return False


    