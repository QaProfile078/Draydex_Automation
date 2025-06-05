Feature: Check Deleted Quote On Rate Quotes Page
  Scenario: Verify deleted Quote is not on Rate Quotes Page
    Given the user is on the dashboard page
    When user move to the rate quotes page
    And the user will check for "ACTIVE/RECENT SPOT QUOTES" table
    And user searches for quote in the table
    Then the user should see "No record found." message in "ACTIVE/RECENT SPOT QUOTES" table
