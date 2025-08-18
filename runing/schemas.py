from pydantic import BaseModel 
from typing import Optional


class UserBase(BaseModel):
    email: str 
    name: str
    is_active: bool = True

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: int 

    class Config:
        from_attributes = True

class Item(BaseModel):
    name: str
    description: str
    price: int
    is_active: bool = True

    class Config:
        from_attributes = True

class ItemCreate(Item):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    is_active: Optional[bool] = None

