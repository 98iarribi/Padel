"""User login feature tests."""

from pytest_bdd import given, scenario, then, when, parsers
import pytest
from padel.scraping.scrapers import Page
from padel.models.models import User

from dotenv import load_dotenv
import os
from loguru import logger
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor
from tests.conftest import _do_login_sync

load_dotenv()


@pytest.fixture(scope="function")
def page():
    class MockPage:
        url = ""
        page: Page = None

    return MockPage()


@contextmanager
def capture_logs(level="INFO"):
    """Capture loguru-based logs."""
    output = []
    handler_id = logger.add(output.append, level=level, serialize=True)
    yield output
    logger.remove(handler_id)


@pytest.mark.xfail(reason="Not implemented yet")
@scenario("login.feature", "Successful login with correct credentials")
def test_successful_login_with_correct_credentials():
    """Successful login with correct credentials."""


@pytest.mark.xfail(reason="Not implemented yet")
@scenario("login.feature", "Unsuccessful login with incorrect credentials")
def test_unsuccessful_login_with_incorrect_credentials():
    """Unsuccessful login with incorrect credentials."""


@given("the user is in the login page")
def _(page):
    """the user is in the login page."""
    page.url = "https://deportes.zizurmayor.es:8443/zonaabo.php"


@when("the user enters invalid credentials", target_fixture="page")
def _(page):
    """the user enters invalid credentials."""
    user = User(
        username="any user",
        password="any password",
    )
    with ThreadPoolExecutor(max_workers=1) as ex:
        result = ex.submit(_do_login_sync, user).result()
    page.url = result.url
    return page


@when("the user enters valid credentials", target_fixture="page")
def _(page):
    """the user enters valid credentials."""
    user = User(
        username=os.getenv("POLIDEPORTIVO_USER"),
        password=os.getenv("POLIDEPORTIVO_PASSWORD"),
    )
    with ThreadPoolExecutor(max_workers=1) as ex:
        result = ex.submit(_do_login_sync, user).result()
    page.url = result.url
    return page


@then(parsers.parse("the {event} by {user} is logged"))
def _(event, user):
    """the <event> is logged."""
    with capture_logs() as logs:
        a = logs
        assert any(event in log for log in logs)
        assert any(user in log for log in logs)


@then("the user is not redirected to the index page")
def _(page):
    """the user is not redirected to the index page."""
    assert page.url != "https://deportes.zizurmayor.es:8443/index.php"


@then("the user is redirected to the index page")
def _(page):
    """the user is redirected to the index page."""
    assert page.url == "https://deportes.zizurmayor.es:8443/index.php"
