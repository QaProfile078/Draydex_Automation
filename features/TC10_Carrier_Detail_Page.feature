Feature: Draydex Web Application - Carrier Management and Dashboard Functionality


  Scenario: Verify that the Dashboard page is displayed after login
    Given the user is on the dashboard page

  Scenario: Verify the "Find & Manage Carriers" heading on the Carriers page
    When User click on the "Carriers" option from the left menu
    Then User should see the "Find & Manage Carriers" heading
    And User should see a list of all carriers in the Draydex application

  Scenario: Verify available sections and options in the Carriers page
#    When User click on the "Carriers" option from the left menu
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


  Scenario: Verify the Carrier Detail Page
#    When User click on the "Carriers" option from the left menu
    And User select a carrier from the list
    Then User should see the following sections on the Carrier Details Page:
      | Carrier Company Name               |
      | MC                                 |
      | DOT                                |
      | Carrier Bulletin                   |
      | General Information             |
      | Primary Contact Information     |
      | Markets and Terminal Service Area  |
    And User should see a "+ Add to Carriers" button
    And User should see a "Block/Ban Carrier" button
