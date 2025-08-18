from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import schemas
import services
'''
sqlalchemy or orm을 사용하여 데이터 베이스 테이블의 구조 정의
이유: 데이터 베이스 구조를 정의해야 이구조를 기반으로 데이터를 주고받을 pydantic 스키마(schemas.py)를,와 데이터 접근로직(repositories.py)을 구현할수있다
'''

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