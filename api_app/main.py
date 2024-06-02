import asyncio
from api_app.database.CRUD import async_main_no_model, async_main_orm, user_create


"asyncio.run(async_main())"
asyncio.run(user_create())
print("start_app")
