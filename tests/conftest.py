from playwright.sync_api import sync_playwright

from padel.models.models import User
from padel.scraping.scrapers import LoginScraper


def _do_login_sync(user: User):
    """Run synchronous Playwright login in a separate thread."""
    pw = sync_playwright().start()
    browser = pw.firefox.launch(headless=True)
    try:
        scraper: LoginScraper = LoginScraper.create(browser=browser)
        result = scraper.login(user=user)
        return result
    finally:
        try:
            browser.close()
        except Exception:
            pass
        try:
            pw.stop()
        except Exception:
            pass
