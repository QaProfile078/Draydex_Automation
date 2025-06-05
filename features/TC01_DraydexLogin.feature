Feature: User Login

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters a valid username and password
    And clicks the login button
    Then the user should be redirected to the dashboard
    
  Scenario: User tries to log in with an invalid username
    Given the user is on the login page
    When the user enters an invalid username and a valid password
    And clicks the login button
    Then the user should see an error message indicating invalid credentials
    And the user should remain on the login page

  Scenario: User tries to log in with an invalid password
    Given the user is on the login page
    When the user enters a valid username and an invalid password
    And clicks the login button
    Then the user should see an error message indicating invalid credentials
    And the user should remain on the login page

  Scenario: User tries to log in with empty username field
    Given the user is on the login page
    When the user leaves the username fields empty
    And clicks the login button
    Then the user should see an error message "The username field is required"

  Scenario: User tries to log in with empty password field
    Given the user is on the login page
    When the user leaves the password fields empty
    And clicks the login button
    Then the user should see an error message "The password field is required."

  Scenario: User tries to log in with empty username & password fields
    Given the user is on the login page
    When the user leaves the username and password fields empty
    And clicks the login button
    Then the user should see an error message "The username field is required"
    And the user should see an error message "The password field is required."

  Scenario: Unsuccessful login with invalid credentials
    Given the user is on the login page
    When the user enters an invalid username or password
    And clicks the login button
    Then the user should see an error message indicating invalid credentials
    And the user should remain on the login page
    
    
    
    
