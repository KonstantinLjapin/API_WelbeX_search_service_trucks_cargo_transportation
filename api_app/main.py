from typing import Annotated
from fastapi import FastAPI, Depends
from config import Settings
from functools import lru_cache

app = FastAPI()


@lru_cache
def get_settings():
    return Settings()


@app.get("/")
async def read_root(settings: Annotated[Settings, Depends(get_settings)]):

    return {"Hello": settings.db_container_name}


