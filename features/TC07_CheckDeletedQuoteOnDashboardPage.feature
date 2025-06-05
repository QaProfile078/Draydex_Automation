Feature: Feature: Check Deleted Quote On Dashboard Page
  Scenario: Verify deleted Quote is not on Dashboard Page
    Given the user is on the dashboard page
    When the user will check for "ACTIVE/RECENT SPOT QUOTES" table
    And user searches for quote in the table
    Then the user should see "No record found." message in "ACTIVE/RECENT SPOT QUOTES" table
