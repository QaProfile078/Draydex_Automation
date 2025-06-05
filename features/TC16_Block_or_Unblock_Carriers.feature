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

  Scenario: Verify the "Block/Ban Carrier" functionality
    When User click on the "Block/Ban Carrier" button
    Then a warning popup should be displayed with message:
      | Warning. This carrier will no longer be able to view your rate requests. |
    And the popup should display "Submit" and "Cancel" buttons
    When User click on the "Submit" button
    Then the carrier should be blocked
    And a message "Carrier Blocked. Carrier is now unable to view/quote your rate request." should be displayed

  Scenario: Verify blocked carrier is highlighted on listing
    When User block a carrier from the details page
    Then the blocked carrier should have a PINK background on the "Carrier Listing Page"

  Scenario: Verify the "Unblock/Unban Carrier" functionality
    Given a carrier is already blocked and has a PINK background
    When User click on that blocked carrier
    And User click on the "Unblock/UnBan Carrier" button
    Then a confirmation popup should appear with the message:
      | Are you sure you want to Unblock Carrier? |
    And the popup should display "Submit" and "Cancel" buttons
    When User click on the "Submit" button
    Then the carrier should be unblocked
    And a message "Carrier unblock successfully." should be displayed






