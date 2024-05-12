from sqlalchemy import create_engine
from sqlalchemy.engine import URL


"postgresql+asyncpg://{config.db.user}:{config.db.password}@{config.db.host}:{config.db.port}/{config.db.name}"

url = URL.create(
    drivername="postgresql",
    username="coderpad",
    host="db",
    database="locator"
)

engine = create_engine(url)

