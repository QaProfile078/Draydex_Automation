Feature: Remove an existing Steamship Lines (Market)

  Scenario: Verify "Settings" Tab and "Manage Market" Button
    Given the user is on the dashboard page
    Then  User should see a "Settings" tab and move to it
    Then the user should see the following options in settings tab:
      | Option              |
      | FallBack Table      |
      | Manage SSL          |
      | Manage Market       |
      | Manage Terminal     |

    When  User click the "Manage Market" button
    Then  User should be taken to the Market management page

  Scenario: Verify Sections in the "Manage Manage/Terminal" Option
#    Given the user is on the "Manage Manage/Terminal" page
    Then the user should see the following sections:
      | Columns          | Buttons            |
      | Market Name      | Add Market         |
      | County           | Remove Market      |
      | State            | Upload CSV         |
      | Name             | Clear              |
      | Zip Code         | Active Markets      |
      |                  | InActive Markets   |

  Scenario: Verify "Remove Market" cancellation Functionality
    When User search for Market from active Market tabel to Remove
    Then User should see Remove Market button is enabled
    When User clicks "Remove Market" button
    Then User should see a Market Removal confirmation Popup with close and confirm buttons
    When User click on "Cancel" to cancel Market Removal
    Then User will click on clear to reset Market table
    And User should see selected Market still in list of active Markets
    And  User will click on clear to reset Market table

  Scenario: Verify "Remove Market" confirmation Functionality
    When User search for Market from active Market tabel to Remove
    Then User should see Remove Market button is enabled
    When User clicks "Remove Market" button
    Then User should see a Market Removal confirmation Popup with close and confirm buttons
    When User click on "Confirm" to confirm Market Removal
    Then User should see "Market(s) move to inactive" popup message
    And User will click on clear to reset Market table
    And User should see selected Market not in list of active Markets

  Scenario: Verify Removed Market is in InActive Market List
    When User click on InActive Market button
    Then the Market removed should be added to the InActive Market table

  Scenario: Verify Created Market in Create Quote/Quote Detail Page
    Given the user is on the "Create Quote/Quote Detail Page"
    Then the user should not see the created market listed in the dropdown
