Feature: Quote Creation

  Scenario: Unsuccessful quote creation due to missing required field values
    Given the user is on the dashboard page
    When the user misses to fill required field for quote creation
    And the user click Create Quote button
    Then the user should see "value is required" in error message under
    And the user will be on dashboard page.


  Scenario: Successful quote creation with mandatory details
#    Given the user is on the dashboard page
    When the user fill all required details for quote creation
    And the user click Create Quote button
    Then the user should see "New Quote Created!" message popup with a quote number
    And User will verify "View Quote" and "Close & Send" on the newly created Quote pop-up
    And the user click "close and send" the message
    And the user will be on dashboard page.


