Feature: Draydex Admin Dashboard Functionality

  Scenario: Verify Options in the "Settings" Menu
    Given the user is on the dashboard page
    Then User should see a "Settings" tab and move to it
    Then the user should see the following options in settings tab:
      | Option              |
      | FallBack Table      |
      | Manage SSL          |
      | Manage Market       |
      | Manage Terminal     |

    When User click the "Manage Market" button
    Then User should be taken to the Market management page

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

  Scenario: Verify Market Creation Message
#    Given the user is on the "Manage Manage/Terminal" page
    When the user clicks on "Add Market" button
    Then the user should see a popup with the following fields:
      | Field   | Description          |
      | Country | Select from dropdown  |
      | State   | Select from dropdown  |
      | Name    | Unique Name           |
      | Zip Code| Enter Zip Code        |
    And there should be a "Save" and "Cancel" button

  Scenario: Verify Required Fields in "Add Market" Popup
    When User leave one or more fields empty
    And click the "Save" button
    Then User should see a error message with "is required" in it

  Scenario: Successful Market creation
    When the user fill all the required fields:
      | Field   | Description          |
      | Country | Select from dropdown  |
      | State   | Select from dropdown  |
      | Name    | Unique Name           |
      | Zip Code| Enter Zip Code        |
    And click the "Save" button
    Then User see a popup with message "Market created"
    And the new Market should be added to the list of active Markets

  Scenario: Verify Created Market in Create Quote/Quote Detail Page
    Given the user is on the "Create Quote/Quote Detail Page"
    Then the user should see the created market listed in the dropdown

#  Scenario: Verify Terminal Creation Message
#    Given the user is on the "Manage Manage/Terminal" page
#    When the user clicks on the "+" icon next to a market
#    Then the user should be able to fill in the following fields:
#      | Field        | Description                  |
#      | Terminal Name| Enter Terminal Name          |
#      | Type         | Select RAIL or MARINE        |
#      | Address      | Enter Address                |
#      | Zip Code     | Enter Zip Code               |
#    And the user clicks "Submit"
#    Then the terminal should be created successfully
#
#  Scenario: Verify Created Terminal in Create Quote/Quote Detail Page
#    Given the user is on the "Create Quote/Quote Detail Page"
#    When the user selects the market under which the terminal is created
#    And clicks on the "Terminal" dropdown
#    Then the user should see the created terminal listed in the dropdown
