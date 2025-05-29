from sqlalchemy import Column, Integer, String, Boolean
from database import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key =True, index =True)
    email = Column(String, unigue=true, index=True)
    name = Column(String)
    is_active = Column(Boolean, default =True)

