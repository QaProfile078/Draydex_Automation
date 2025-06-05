Feature: Create a new Steamship Lines (SSL)
  
  Scenario: Verify "Settings" Tab and "Manage SSL" Button
    Given the user is on the dashboard page
    Then User should see a "Settings" tab and move to it
    Then the user should see the following options in settings tab:
      | Option            |
      | FallBack Table    |
      | Manage SSL        |
      | Manage Market     |
      | Manage Terminal   |

    When User click the "Manage SSL" button
    Then User should be taken to the SSL management page

  Scenario: Verify "Add SSL" Button Functionality
    When User click the "Add SSL" button
    Then User should see a popup with the following fields:
      | SSL Name         |
      | SCAC Code        |
      | Abbreviated Name |
    And there should be a "Save" and "Cancel" button

  Scenario: Verify Validation for Required Fields in "Add SSL" Popup
    When User leave one or more fields empty
    And click the "Save" button
    Then User should see a error message with "is required" in it

  Scenario: Verify "Save" Button in "Add SSL" Popup
    When User fill in all fields (SSL Name, SCAC Code, Abbreviated Name)
    And click the "Save" button
    Then User see a popup with message "SSL created"
    And the new SSL should be added to the list of active SSLs
