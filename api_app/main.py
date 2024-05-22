from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine, Engine
from sqlalchemy import select
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

import asyncio


class Settings(BaseSettings):
    postgres_host: str
    postgres_user: str
    postgres_db: str
    postgres_port: str
    postgres_password: str
    db_container_name: str


settings: Settings = Settings()
asyncpg_engine: str = "asyncpg"
psycopg2_engine: str = "psycopg2"
DATABASE_URL = (f"postgresql+{asyncpg_engine}://{settings.postgres_user}:{settings.postgres_password}@"
                f"{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}")

"""engine = create_async_engine(DATABASE_URL)"""

meta = MetaData()
t1 = Table("t1", meta, Column("name", String(50), primary_key=True))


async def async_main() -> None:
    engine = create_async_engine(DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)
        await conn.execute(
            t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
        )
    async with engine.connect() as conn:
        # select a Result, which will be delivered with buffered
        # results
        result = await conn.execute(select(t1))
        print(result.fetchall())
    # for AsyncEngine created in function scope, close and
    # clean-up pooled connections
    await engine.dispose()


asyncio.run(async_main())

print("start_app")
