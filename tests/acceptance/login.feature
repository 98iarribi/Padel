Feature: User login  

  Scenario: Successful login with correct credentials
    Given the user is in the login page
    When the user enters valid credentials
    Then the user is redirected to the index page
    And the <event> is logged

    Examples:
      | event           |
      | login_succeeded |
    
  Scenario: Unsuccessful login with incorrect credentials
    Given the user is in the login page
    When the user enters invalid credentials
    Then the user is not redirected to the index page
    And the <event> is logged

    Examples:
      | event        |
      | login_failed |