from sqlalchemy.orm import Session
from .models import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email: str, username: str, hashed_password: str):
        db_user = User(email=email, username=username, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def delete_user(self, user: User):
        self.db.delete(user)
        self.db.commit()