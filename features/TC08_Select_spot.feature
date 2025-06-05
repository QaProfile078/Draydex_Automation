Feature: Verify functionality of the Select Spot popup

   Scenario: Verify the Dashboard Page
    Given the user is on the dashboard page

  Scenario: Verify the Rate Quotes Page
    When user move to the rate quotes page
    And the user will check for "ACTIVE/RECENT SPOT QUOTES" table

  Scenario: Verify the Quote Detail Page
    When user searches for quote in the table
    And  user should see the quote in the table on current page
    Then the user will click on quote id
    And the following buttons should be displayed:
      | Send to Carriers |
      | Add Rate         |
      | Update Changes   |
      | Void Quote       |

  Scenario: Verify presence of labels in the "Select Spot" popup
#    Given the user will go to the Rate Quotes page
#    When User open the "Select Spot" popup
    When User click on "Select Spot"
    Then User should see the label "ESTIMATED TOTAL:" at the bottom of the Carrier Charge column
    And User should see the label "GROSS MARGIN:" at the bottom of the Carrier Charge column

  Scenario: Verify non-editable sum and difference fields
#    Given the user will go to the Rate Quotes page
#    When User open the "Select Spot" popup
    Then User will verify the "Estimated Total" field is non-editable
    And User will verify the "Gross Margin" field is non-editable

  Scenario: Verify display of sum of "Your Charge" in "Estimated Total"
#    Given the user will go to the Rate Quotes page
#    When User open the "Select Spot" popup
    When User check the "Your Charge" and "Carrier Charges" column
    Then User view the sum of "Your Charge" in "Estimated Total"
#
  Scenario: Verify display of "Gross Margin"
#    Given the user will go to the Rate Quotes page
#    When User open the "Select Spot" popup
#    When User check the "Your Charge" and "Carrier Charges" column
#    Then User view the sum of "Your Charge" in "Estimated Total"
    Then User should see the difference between sum of "Your Charge" and sum of "Carrier Charge" in "Gross Margin"


Scenario: Verify dynamic update of sum and difference when charges change
#    Given the user will go to the Rate Quotes page
#    When  User open the "Select Spot" popup
#    Then  User should see the label "ESTIMATED TOTAL:" at the bottom of the Carrier Charge column
#    And   User should see the label "GROSS MARGIN:" at the bottom of the Carrier Charge column
#    And   User will verify the "Estimated Total" field is non-editable
#    And   User will verify the "Gross Margin" field is non-editable
#    When  User check the "Your Charge" and "Carrier Charges" column
#    Then  User view the sum of "Your Charge" in "Estimated Total"
#    And   User should see the difference between sum of "Your Charge" and sum of "Carrier Charge" in "Gross Margin"
    When  User change one or more charges in the "Your Charge" column
    Then  User should see the "Estimated Total" column update automatically
    And   User should see the "ESTIMATED TOTAL" recalculate based on the new charges
    And   User should see "GROSS MARGIN" update dynamically
    And   User should see the "GROSS MARGIN" recalculate based on the new charges

Scenario: Send Marked-Up Quote
    When  User verifies Email field present at the bottom of popup
    Then  User will enter an email id into the field
    When  User will submit the updated values
    Then  User will see "Quote Rated successfully" message
    Then  User will see an entry with updated values having green background

Scenario: Verify the email received
    When  User will switch to another window
    And   User open email id entered during Mark-up
    Then  User will see an email recieved from draydex
    When  User checks if the email is received.
    Then  User should see Quote number and different informations
    And   User Verifies all the infromations are correct


