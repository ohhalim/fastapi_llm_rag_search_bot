from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:qwe123@localhost:5432/fastapi_rag"
    app_name: str = "FastAPI simple REST API"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
