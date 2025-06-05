from sqlalchemy import Column, Integer, String, Boolean
from database import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key =True, index =True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default =True)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key =True, index =True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    is_active = Column(Boolean, default =True)