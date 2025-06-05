Feature: Quote Creation and Carrier Notification Flow

  Scenario: Verify the Dashboard page loads successfully
    Given the user is on the dashboard page

  Scenario: Fetch Data of favourite carriers
    When User click on the "Carriers" option from the left menu
    Then User should see the "Find & Manage Carriers" heading
    When User click on "My Carrier"
    Then User should see List of favorite carriers
    And User will fetch data of favorite of carriers

  Scenario: Create a new quote and verify confirmation
    Given the user is on the dashboard page
    When the user fill all required details for quote creation
    And User select the Market same as that of favourite carrier
    And the user click Create Quote button
    Then the user should see "New Quote Created!" message popup with a quote number

  Scenario: Verify "View Quote" and "Close & Send" buttons on quote popup
    Then User will verify "View Quote" and "Close & Send" on the newly created Quote pop-up

  Scenario: Click on "Close & Send" and verify email is sent to carrier
    Then the user click "close and send" the message
    And the user will be on dashboard page.

  Scenario: Verify the Quote Detail Page
    When the user will check for "ACTIVE/RECENT SPOT QUOTES" table
    When user searches for quote in the table
    And user should see the quote in the table on current page
    Then the user will click on quote id
    And the following buttons should be displayed:
      | Send to Carriers |
      | Add Rate         |
      | Update Changes   |
      | Void Quote       |
    And the user will verify all the details of the quote

  Scenario: Verify the "E-mail Spot Quote Request to Your Carriers" pop-up
    When User clicks on "Send to Carriers"
    Then the "E-mail Spot Quote Request to Your Carriers" pop-up should display
    And the following columns should be displayed:
      | Include     |
      | Sent?       |
      | Carrier Name|
      | Phone#      |
      | Email       |
      | Other Email |

  Scenario: Verify the "Send to Carrier" section reflects sent mail
    Then User should see that the favorite carrier has received the "Carrier Mail" under the "Send to Carrier" section
