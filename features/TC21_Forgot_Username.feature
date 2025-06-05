Feature: Retrieve Username Using Forgot Username
  Scenario: Invalid retrieval of Username without filling any field
    Given the user is on the login page
    When the user clicks on "Forgot Username" button
    Then the user is on Forgot Username Page
    When User clicks on "Request To Get username" button
    Then the user should see error messages under required field

  Scenario: Successful retrieval of username with required field
    Given the user is on the login page
    When the user clicks on "Forgot Username" button
    Then the user is on Forgot Username Page
    When User fills all required data fields
    And User clicks on "Request To Get username" button
    Then the user should get a mail with their username

  Scenario: User tries to login with Username received on mail
    Given the user is on the login page
    When User enters the username recieved in email
    And User enters correct password
    Then the user is logged in successfully