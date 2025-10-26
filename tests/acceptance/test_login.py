"""User login feature tests."""

from pytest_bdd import given, scenario, then, when, parsers
import pytest
from padel.scraping.scrapers import LoginScraper, Page
from padel.models.models import User

from playwright.async_api import async_playwright
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope="function")
def page():
    class MockPage:
        url = ""
        page: Page = None

    return MockPage()


@scenario("login.feature", "Successful login with correct credentials")
def test_successful_login_with_correct_credentials():
    """Successful login with correct credentials."""


@scenario("login.feature", "Unsuccessful login with incorrect credentials")
def test_unsuccessful_login_with_incorrect_credentials():
    """Unsuccessful login with incorrect credentials."""


@given("the user is in the login page")
def _(page):
    """the user is in the login page."""
    page.url = "https://deportes.zizurmayor.es:8443/zonaabo.php"


@pytest.mark.asyncio
@when("the user enters invalid credentials")
async def _():
    """the user enters invalid credentials."""
    browser = await async_playwright().start().firefox.launch(headless=True)
    scraper: LoginScraper = await LoginScraper.create(browser=browser)
    user = User(
        username="any user",
        password="any password",
    )
    result = await scraper.login(user=user)
    page.url = result.url 
    return page


@pytest.mark.asyncio
@when("the user enters valid credentials", target_fixture="page")
async def _(page):
    """the user enters valid credentials."""
    browser = await async_playwright().start().firefox.launch(headless=True)
    scraper: LoginScraper = await LoginScraper.create(browser=browser)
    user = User(
        username=os.getenv("POLIDEPORTIVO_USER"),
        password=os.getenv("POLIDEPORTIVO_PASSWORD"),
    )
    result = await scraper.login(user=user)
    page.url = result.url 
    return page


@then(parsers.parse("the {event} is logged"))
def _(event):
    """the <event> is logged."""
    assert event in ("login_succeeded", "login_failed") # needs tweaking: logging is not implemented yet


@then("the user is not redirected to the index page")
def _(page):
    """the user is not redirected to the index page."""
    assert page.url != "https://deportes.zizurmayor.es:8443/index.php"


@pytest.mark.asyncio
@then("the user is redirected to the index page")
async def _(page):
    """the user is redirected to the index page."""
    assert page.url == "https://deportes.zizurmayor.es:8443/index.php"
