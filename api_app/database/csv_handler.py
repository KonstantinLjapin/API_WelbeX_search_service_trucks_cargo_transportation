import aiofiles
from typing import AsyncGenerator
from aiocsv import AsyncDictReader
from api_app.database.schemas import Location


class CsvHandler:

    def __init__(self, in_file: str):
        """
        Main function that reads lines from in_file, parses them and saves to out_file.
        """
        self.raw_line_generator = self.read_lines(in_file)
        self.parsed_line_generator = self.parse_lines(generator=self.raw_line_generator)

    async def read_lines(self, file: str) -> AsyncGenerator[dict, None]:
        """
        Read lines from CSV file.
        """
        async with aiofiles.open(file, "r") as afp:
            async for row in AsyncDictReader(afp, delimiter=","):
                yield row

    async def parse_lines(self, generator: AsyncGenerator[dict, None]) -> AsyncGenerator[dict, None]:
        """
        Parse lines from generator.
        """
        async for line in generator:
            # do some parsing here, like that:
            yield Location.model_validate(line)


async def gen_csv_handler(in_file: str) -> CsvHandler:
    return CsvHandler(in_file)


async def main(in_file: str) -> None:
    m = await gen_csv_handler(in_file)
    async for i in m.parsed_line_generator:
        print(i)
