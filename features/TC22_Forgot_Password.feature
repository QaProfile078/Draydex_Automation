Feature: Draydex Application - Password Management

  Scenario: Verify the Forgot Password Page
    Given the user is on the login page
    When the user clicks on the "Forgot Password?" link
    Then the "Forgot Password" page should be displayed with mandatory fields

  Scenario: Verify Forgot Password Email Functionality
    Given the user is on the login page
    When the user clicks on the "Forgot Password?" link
    And enters a valid email address
    And User selects valid user type
    And clicks the "REQUEST RESET LINK" button
    Then the user should see the message "If this email exists, you will receive a reset email."

  Scenario: Verify Email to Reset Password
    When  User will switch to another window
    And   User open email id entered during Mark-up
    Then  User will see an email recieved from draydex
    When  User checks if the email is received.
    Then  User should receive a "Forgot Password" email with a "Reset Password" button

  Scenario: Verify Reset Password Functionality
    When receives the "Forgot Password" email
    And clicks on the "Reset Password" link in the email
    Then the user should see fields "Enter new Password","Confirm your Password" and "Enter Username"
    And the user should be able to click the "Update Password" button
    Then the message "Your Password has been changed!" should be displayed

  Scenario: Verify Login with new password
    Given the user is on the login page
    When the user enters the username and new password
    And clicks the login button
    Then the user should be redirected to the dashboard