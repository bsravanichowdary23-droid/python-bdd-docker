Feature: Login functionality

  Scenario: Successful login
    Given the login page is available
    When the user enters valid credentials
    Then the user should see a successful login message