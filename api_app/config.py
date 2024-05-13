from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_host: str
    postgres_user: str
    postgres_db: str
    postgres_port: str
    postgres_password: str
    db_container_name: str
