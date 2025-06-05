Feature: Update Quotes details Functionality for Draydex

  Scenario: Verify the "Update Changes" button is enabled after modifying the quote
    When User modify a value in the Quote Detail page
    Then the "Update Changes" button should be enabled

  Scenario: Verify the "You Have Updated the Details of This Quote!" pop-up and re-send functionality
    And  User click on the "Update Changes" button
    Then User should see a pop-up with message "You Have Updated the Details of This Quote!"
    When User click on "View Log" button
    Then User should see log of updated data in it
    And Store the Quotes updated data


