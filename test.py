import httpx
import asyncio
import time
from bs4 import BeautifulSoup
import lxml

async def fetch_fixtures(URL):
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        print(response.text)
    page = BeautifulSoup(response.text, "lxml")
    fix = page.find_all("li", class_="simple-match-cards-list__match-card")
    print(fix)

async def main():
    start = time.perf_counter()
    URLS = ['https://onefootball.com/en/competition/premier-league-9/fixtures', 'https://onefootball.com/en/competition/laliga-10/fixtures']
    coros = []
    for URL in URLS:
        coros.append(fetch_fixtures(URL))
    await asyncio.gather(*coros)
    end = time.perf_counter()
    print(f"Time taken to finish execution: {end-start:.2f}")

asyncio.run(main())