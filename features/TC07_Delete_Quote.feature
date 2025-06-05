Feature: Delete Existing Quote
  Scenario: Successful deletion of newly created quote
    Given the user is on the dashboard page
    When user move to the rate quotes page
    When the user will check for "ACTIVE/RECENT SPOT QUOTES" table
    And user searches for quote in the table
    And user should see the quote in the table on current page
    Then the user will click on quote id
    And the user will click on "Void Quote" to delete the quote
    And the user will be on dashboard page.



