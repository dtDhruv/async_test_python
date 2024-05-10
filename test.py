import aiohttp
import asyncio
import time

async def fetch_fixtures(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            html = await response.text()
            print(html)

async def main():
    start = time.perf_counter()
    URLS = ['https://www.premierleague.com/fixtures', 'https://www.skysports.com/la-liga-fixtures']
    coros = []
    for URL in URLS:
        coros.append(fetch_fixtures(URL))
    await asyncio.gather(*coros)
    end = time.perf_counter()
    print(f"Time taken to finish execution: {end-start:.2f}")

asyncio.run(main())