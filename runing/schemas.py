from pydantic import BaseModel 
from typing import Optional

class UserBase(BaseModel):
    email: str 
    name: str
    is_active: bool = True

class UserCreate(UserBase):
    pass

class UserUpdate(baseModel):
    email: Optional(str) = None
    name: Optional(str) = None
    is_active: Optional(bool) = None

class User(UserBase):
    id: int 

    class Config:
        from_attributes = True

