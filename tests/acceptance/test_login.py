"""User login feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
import pytest

@pytest.mark.xfail(reason="Not implemented yet")
@scenario('login.feature', 'Successful login with correct credentials')
def test_successful_login_with_correct_credentials():
    """Successful login with correct credentials."""


@pytest.mark.xfail(reason="Not implemented yet")
@scenario('login.feature', 'Unsuccessful login with incorrect credentials')
def test_unsuccessful_login_with_incorrect_credentials():
    """Unsuccessful login with incorrect credentials."""


@given('the user is in the login page')
def _():
    """the user is in the login page."""
    raise NotImplementedError


@when('the user enters invalid credentials')
def _():
    """the user enters invalid credentials."""
    raise NotImplementedError


@when('the user enters valid credentials')
def _():
    """the user enters valid credentials."""
    raise NotImplementedError


@then('an error message should be displayed')
def _():
    """an error message should be displayed."""
    raise NotImplementedError


@then('the <event> is logged')
def _():
    """the <event> is logged."""
    raise NotImplementedError


@then('the user should be redirected to the main page')
def _():
    """the user should be redirected to the main page."""
    raise NotImplementedError

