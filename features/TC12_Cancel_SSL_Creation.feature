Feature: Cancel a new Steamship Lines (SSL) creation

  Scenario: Verify "Settings" Tab and "Manage SSL" Button
    Given the user is on the dashboard page
    Then User should see a "Settings" tab and move to it
    And within the "Settings" tab, User should see a "Manage SSL" button
    When User click the "Manage SSL" button
    Then User should be taken to the SSL management page

  Scenario: Verify "Add SSL" Button Functionality
    When User click the "Add SSL" button
    Then User should see a popup with the following fields:
      | SSL Nise         |
      | SCAC Code        |
      | Abbreviated Nise |
    And there should be a "Save" and "Cancel" button

  Scenario: Verify "Cancel" Button in "Add SSL" Popup
    When User fill in all fields (SSL Name, SCAC Code, Abbreviated Name)
    And click the "Cancel" button
    Then the "Add SSL" popup should close
    And the SSL should not be created and added to the list of active SSLs
