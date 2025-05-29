from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import schemas
import services

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    username = Column(String(30), unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(username={self.username})>"