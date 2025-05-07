from fastapi import FastAPI
from .routers import router
from .database import engine, Base

app = FastAPI()

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/users", tags=["users"])