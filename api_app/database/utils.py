from sqlalchemy import create_engine
from api_app.config import Settings
from functools import lru_cache


"""@lru_cache
def get_settings():
    return Settings()


settings = get_settings()


engine = create_engine(f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@"
                       f"{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}")"""

print("ok")
