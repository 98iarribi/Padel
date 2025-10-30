import re
from padel.models.models import User
from playwright.async_api._generated import Browser, BrowserContext, Page
from padel.utils import PadelLogger


class LoginScraper:
    LOGIN_URL = "https://deportes.zizurmayor.es:8443/zonaabo.php"
    INDEX_PAGE = "https://deportes.zizurmayor.es:8443/index.php"

    def __init__(self, browser: Browser, context: BrowserContext):
        self.browser = browser
        self.context = context
        self.logger = PadelLogger()

    @classmethod
    async def create(cls, browser: Browser) -> "LoginScraper":
        """Async factory method to initialize LoginScraper."""
        context = await browser.new_context()
        return cls(browser, context)

    async def login(self, user: User):
        """Logs in a user with given credentials."""
        page = await self._open_login_page()
        page = await self._submit_login_form(page, user)
        self.logger.info(event="user_login", user=user.username)
        return page

    async def _open_login_page(self):
        """Opens the login page."""
        page = await self.context.new_page()
        await page.goto(self.LOGIN_URL)
        return page

    async def _submit_login_form(self, page: Page, user: User):
        """Fills the login form with user credentials."""
        await page.fill("#usuario", user.username)
        await page.fill("#password", user.password)
        await page.click("#validar")
        await page.goto(self.INDEX_PAGE)
        return page
