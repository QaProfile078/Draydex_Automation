Feature: Remove an existing Steamship Lines (SSL)

  Scenario: Verify "Settings" Tab and "Manage SSL" Button
    Given the user is on the dashboard page
    Then  User should see a "Settings" tab and move to it
    And   the user should see the following options in settings tab
    When  User click the "Manage SSL" button
    Then  User should be taken to the SSL management page
    And   User verifies different elements present on this page

  Scenario: Verify "Remove SSL" cancellation Functionality
    When User select first SSL from active SSL tabel
    Then User should see Remove SSl button is enabled
    When User clicks "Remove SSl" button
    Then User should see a SSL Removal confirmation Popup with close and confirm buttons
    When User click on "Cancel" to cancel SSL Removal
    Then User should see selected SSL still in list of active SSLs
    And User will click on clear to reset table

  Scenario: Verify "Remove SSL" confirmation Functionality
    When User select first SSL from active SSL tabel
    Then User should see Remove SSl button is enabled
    When User clicks "Remove SSl" button
    Then User should see a SSL Removal confirmation Popup with close and confirm buttons
    When User click on "Confirm" to confirm SSL Removal
    Then User should see "SSL(s) move to inactive" popup
    Then User should see selected SSL not in list of active SSLs

  Scenario: Verify Removed SSL is in InActive SSL List
    When User click on InActive SSL button
    Then the SSL removed should be added to the InActive SSL table
