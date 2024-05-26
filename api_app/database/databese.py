from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select
from api_app.config import db_settings
from api_app.database.models import meta, t1


def make_connection_string() -> str:
    """
    Make connection string to db
    """
    asyncpg_engine: str = "asyncpg"
    return (f"postgresql+{asyncpg_engine}://{db_settings.postgres_user}:{db_settings.postgres_password}@"
            f"{db_settings.postgres_host}:{db_settings.postgres_port}/{db_settings.postgres_db}")


async def async_main() -> None:
    engine = create_async_engine(make_connection_string(), echo=False)
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
