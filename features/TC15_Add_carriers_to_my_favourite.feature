Feature: Carrier Management Functionality

  Scenario: Verify Dashboard Page Loads
    Given the user is on the dashboard page

  Scenario: Verify "Find & Manage Carriers" Heading
    When User click on the "Carriers" option from the left menu
    Then User should see the "Find & Manage Carriers" heading

  Scenario: Verify Sections in "Carriers" Tab
    Then User should see the following radio button options:
      | 20/40FT  |
      | 53FT     |
      | HAZ      |
      | TRANSLOAD|
      | CHASSIS  |
      | BONDED   |
      | PARKING  |

    And User should see the following column headers:
      | Carrier Company Name |
      | Location             |
      | Service State        |
      | Market               |
      | Port/Terminal        |
      | Phone                |
      | Entity Type          |

  Scenario: Verify Carrier Detail Page
    And User select a carrier from the list
    Then User should see the following sections on the Carrier Details Page:
      | Carrier Company Name               |
      | MC                                 |
      | DOT                                |
      | Carrier Bulletin                   |
      | General Information                |
      | Primary Contact Information        |
      | Markets and Terminal Service Area  |
    And User should see a "+ Add to Carriers" button
    And User should see a "Block/Ban Carrier" button

  Scenario: Verify Add Carrier Functionality
    When User click on "+ Add to Carriers"
    Then User should see a confirmation popup with buttons "Confirm" and "Close"
    When User click on "Confirm"
    Then User should see a message "Added to carriers successfully"

  Scenario: Verify My Carrier Functionality
    When User click on the "Back" button to return to the "Carriers Listing Page"
    And User click on "My Carrier"
    Then User should see the favorite carriers with a BLUE background

  Scenario: Verify Update Carrier List Functionality
    When User select one or more carriers using the checkboxes
    Then the "Update Carrier List" button should be enabled
    When User click on "Update Carrier List"
    Then User should see a message "My Carrier list updated successfully"
    And the selected carriers should appear under "My Carrier"

  Scenario: Verify Remove Carrier from Favorites
    When User remove a carrier from the detail page by clicking "+ Remove as My Carrier" Or User deselect carriers in the listing page and click "Update Carrier List"
    Then the carrier should be removed from "My Carrier"
