Feature: Verify Dashboard and Clients Functionality
#
#  Scenario: Verify that the "Dashboard" page is displayed after login
#    Given the user is on the dashboard page
#
#  Scenario: Verify the sections present in the "Clients" option
#    When User click on the "Clients" option present on the left menu
#    Then User should see the following buttons:
#      | Add Client           |
#      | Cancellation Request |
#      | Approval Request     |
#      | Edit View            |
#      | Clear                |
#    And User should see the following column names:
#      | Client Name         |
#      | User Name           |
#      | DOT Number          |
#      | Status              |
#      | MC Number           |
#      | Email Address       |
#      | Client Type         |
#      | City                |
#      | State               |
#      | Subscriber Type     |
#      | Number of Sub-Users |
#      | Active Users        |
#      | Claim Status        |
#      | Phone Number        |
#
#  Scenario: Verify the listing in the "Clients" option
##    When User click on the "Clients" option present on the left menu
#    Then User should see a list of all registered users including customers and carriers
#
#  Scenario: Display correct options based on client type
#    When User selects a client from the list
#    Then User should see appropriate options based on the client type:
#      |      For Carrier             |      For Customer             |
#      | General Information          |  General Information          |
#      | Billing Information Details  |  Billing Information Details  |
#      | Subscription Details         |  Subscription Details         |
#      | Business Address             |  Associated Users             |
#      | Carrier Details              |                               |
#      | Primary Business Contact     |                               |
#      | Associated Users             |                               |
#    And User should see Support options:
#      | Send the Username to the user            |
#      | Send the Password Reset LINK to the user |

  Scenario: Verify if Draydex Admin can update client information
    When User update any available section
    And User save the changes
    Then the updated information should be visible to the client in their "My Profile" section

