from padel.models.models import User
from playwright.sync_api._generated import Browser, BrowserContext, Page
from loguru import logger


class LoginScraper:
    LOGIN_URL = "https://deportes.zizurmayor.es:8443/zonaabo.php"

    def __init__(self, browser: Browser, context: BrowserContext):
        self.browser = browser
        self.context = context

    @classmethod
    def create(cls, browser: Browser) -> "LoginScraper":
        """Factory method to initialize LoginScraper."""
        context = browser.new_context()
        return cls(browser, context)

    def login(self, user: User):
        """Logs in a user with given credentials."""
        page = self._open_login_page()
        page = self._submit_login_form(page, user)
        return page

    def _open_login_page(self):
        """Opens the login page."""
        page = self.context.new_page()
        page.goto(self.LOGIN_URL)
        return page

    def _submit_login_form(self, page, user: User):
        """Fills the login form with user credentials."""
        page.fill("#usuario", user.username)
        page.fill("#password", user.password)
        page.click("#validar")

        logger.info(f"Attempting login for user: {user.username}")
        return page
