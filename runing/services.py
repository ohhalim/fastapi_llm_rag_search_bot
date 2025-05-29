from typing import List, Optional
from fastapi import HTTPException
import schemas
from repoitories import UserRepository

class UserServuce:
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

    def get_user(self, skip: int = 0, limit: int = 100) -> List[schemas.User]:
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



