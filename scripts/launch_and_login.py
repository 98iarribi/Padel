from padel.scraping.scrapers import LoginScraper
from padel.models.models import User
from playwright.async_api import async_playwright
from dotenv import load_dotenv
import os

load_dotenv()

async def main():

    async with async_playwright() as playwright:
        browser = await playwright.firefox.launch(headless=False)

        user = User(os.getenv("POLIDEPORTIVO_USER"), os.getenv("POLIDEPORTIVO_PASSWORD"))
        scraper = await LoginScraper.create(browser)
        page = await scraper.login(user)
        await asyncio.sleep(2)
        await browser.close()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())