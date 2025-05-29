from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://your_user:your_password@your_host:your_port/your_database"
    app_name: str = "FastAPI simple REST API"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
