from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
'''
데이터베이스 연결을 설정하고 . 세션을 관리하는 코드를 포함
sqlalchemy, create_engine, sessionmaker, base 설정
이유: models.py에서 정의된 모델이 실제로 데이터베이스와 상호 작용하기위한 연결, 세션관리 록직, -> repositories.py에서 이 세션을 사용함
'''

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # 예시로 SQLite 사용

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


