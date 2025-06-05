Feature: Draydex Rate Quote Management

  Scenario: Verify the "Are you sure you want to delete this Rate?" confirmation
    When User click the "Delete" button next to a rate
    Then User should see a confirmation popup with message "Are you sure you want to delete this Rate?"
    And User should see "Yes" and "No" buttons

  Scenario: Verify the "Rate delete successfully" message
    When User confirm the rate deletion by clicking "Yes"
    Then User should see a message "Rate delete successfully"
    And the deleted rate should not appear in the quote
