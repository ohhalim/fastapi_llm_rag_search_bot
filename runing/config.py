from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # TODO: YOUR_PASSWORD 부분을 실제 postgres 사용자 비밀번호로 변경하세요.
    database_url: str = "postgresql://postgres:qwe123@localhost:5432/fastapi_rag"
    app_name: str = "FastAPI simple REST API"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
