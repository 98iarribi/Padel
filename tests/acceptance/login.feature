Feature: User login  

  Scenario: Successful login with correct credentials  
    Given the user is in the login page
    When the user enters valid credentials
    Then the user should be redirected to the main page
    And the <event> is logged

    Examples:
      | event           |
      | login_succeeded |
    
  Scenario: Unsuccessful login with incorrect credentials  
    Given the user is in the login page
    When the user enters invalid credentials
    Then an error message should be displayed
    And the <event> is logged

    Examples:
      | event        |
      | login_failed |