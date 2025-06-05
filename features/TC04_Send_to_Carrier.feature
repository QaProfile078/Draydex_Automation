Feature: Draydex Application - Send Quote Details to Carrier

  Scenario: Verify the Quote Detail Page
    Given the user is on the dashboard page
    When user move to the rate quotes page
    When the user will check for "ACTIVE/RECENT SPOT QUOTES" table
    And user searches for quote in the table
    And user should see the quote in the table on current page
    Then the user will click on quote id
    And the following buttons should be displayed:
      | Send to Carriers |
      | Add Rate         |
      | Update Changes   |
      | Void Quote       |
    And the user will verify all the details of the quote


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
    And User should be able to check the "Include" column to send an email to a particular carrier or select the "Select ALL" checkbox to send the email to all carriers
    And User should be able to press the "Submit" button to send the email to a carrier

#  Scenario: Verify the "Sent?" Status
#    When User presses the "Submit" button
#    When User should see "Mail sent to carrier" popup message
#    And   User clicks on "Send to Carriers"
#    Then the "Sent?" status should be displayed as "Yes" for all the carriers to which mail has been sent
