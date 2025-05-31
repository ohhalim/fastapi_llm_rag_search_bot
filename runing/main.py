from fastapi import FastAPI
from config import settings
from database import engine
from routers import router
import models

# 데이터베이스 테이블 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

# 라우터 등록
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Simple REST API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)