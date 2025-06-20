Feature: Draydex Application - Send Quote Details to Carrier

  Scenario: Verify the "E-mail Spot Quote Request to Your Carriers" pop-up
    When User clicks on "Send to Carriers"
    Then the "E-mail Spot Quote Request to Your Carriers" pop-up should display
    And the following columns should be displayed:
      | Include     |
      | Sent?       |
      | Carrier Name|
      | Phone#      |
      | Email       |
      | Other Email |

  Scenario: Verify the "Mail Sent Successfully" message
    When User enters a Carrier Name in the "Carrier Name" field and selects a carrier
    Then the system should automatically fetch the selected carrier's Phone# and Email
    And User should be able to enter an email in the "Other Email" section
    And User should be able to select multiple carriers using Add more button
    And User should be able to check the "Include" column
    And User should be able to press the "Submit" button to send the email to a carrier

  Scenario: Verify the "Sent?" Status
    When User presses the "Submit" button
    When User should see "Mail sent to carrier" popup message
    And  User clicks on "Send to Carriers"
    Then the "Sent?" status should be displayed as "Yes"

  Scenario: Verify the email received by carrier
    When  User will switch to another window
    When  User open email id entered in other email field
    Then  User will see an email recieved from draydex
    When  User checks if the email is received.
    Then  User should see Quote number and different informations
    And   User Verifies all the infromations are correct


