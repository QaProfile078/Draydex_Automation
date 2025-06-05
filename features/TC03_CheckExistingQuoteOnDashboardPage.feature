Feature:  Verify Existing Quote On Dashboard Page

  Scenario: Check created quote on dashboard "ACTIVE/RECENT SPOT QUOTES" table
    Given the user is on the dashboard page
    When the user will check for "ACTIVE/RECENT SPOT QUOTES" table
    When user searches for quote in the table
    And user should see the quote in the table on current page
    Then the user will click on quote id
    And the following buttons should be displayed:
      | Send to Carriers |
      | Add Rate         |
      | Update Changes   |
      | Void Quote       |
