Feature: Add_Rate To A Quote
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

  Scenario: Verify the "Manually Add Carrier Spot Rate" popup
    When User click on "Add Rate"
    Then User should see the "Manually Add Carrier Spot Rate" popup with mandatory fields:
      | Carrier Name / DOT#        |
      | Linehaul($)                |
      | FSC (%)                    |
      | Chassis ($/day)            |
      | Min. Chassis Day           |
      | Add Accessorials           |
      | Carrier has Capacity?      |
      | Earliest Capacity?         |
      | Note                       |
      | Submit button              |
      | Cancel button              |

  Scenario: Verify Error messages while Adding rate without filling mandatory fiels
    When  user clicks on submit button without filling the required fields
    Then  User should see errors under the Required fields

  Scenario: Verify the "Carrier spot rate added successfully" message
    When User fill all the required field and click on submit
    Then the user will see a message with "rate added successfully" in it

  Scenario: Verify the rate posted in the table
    Then Verify the Added rate is visible in Rate Quote Table list
    And User should see the following columns and buttons populated:
      | Date           |
      | Provided By    |
      | Carrier        |
      | Rate Summary   |
      | Accessorial    |
      | Estimated Total|
      | Capacity       |
      | Notes          |
      | Select button  |
      | Delete button  |
