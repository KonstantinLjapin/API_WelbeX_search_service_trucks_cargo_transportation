import asyncio
from api_app.database.CRUD import async_main_no_model, async_main_orm


"asyncio.run(async_main())"
asyncio.run(async_main_orm())
print("start_app")
