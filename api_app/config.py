"""from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_host: str
    postgres_user: str
    postgres_db: str
    postgres_port: str
    postgres_password: str
    db_container_name: str


settings = Settings()

DATABASE_URL = (f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@"
                f"{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}")"""
