import asyncio
from api_app.database.csv_handler import main


in_file = "/api_app/uszips.csv"
asyncio.run(main(in_file))
