##-----------------------------------------------------------------------------------------------------------------------##
##--------------------------------------------- Not Part of Testing Suit ------------------------------------------------##
##-----------------------------------------------------------------------------------------------------------------------##

#Feature: Verify Different filters on Rate Quotes Page
#  Scenario: Successful verification of filtering of Quote present
#    Given the user will go to the Rate Quotes page
#    When  the user verifies fields of Rate Quotes page
#    And   click on Quote id placeholder filter field
#    And   the user enter a quote id
#    Then  the user should see only that specific Quote id in the table
#
#  Scenario: Successful verification of filtering of Requestor
#    Given the user will go to the Rate Quotes page
#    When  the user verifies fields of Rate Quotes page
#    And   click on Requested By placeholder filter field
#    Then  the user enter a Requestor name
#    And   the user should see data related to that specific Requestor only in the table
#
#  Scenario: Successful verification of filtering of Origin/Destination
#    Given the user will go to the Rate Quotes page
#    When  the user verifies fields of Rate Quotes page
#    And   click on Origin/Destination placeholder filter field
#    Then  the user enter a Origin/Destination
#    And   the user should see data related to entered Origin/Destination only in the table
#
#  Scenario: Successful verification of filtering of Roundtrip Miles
#    Given the user will go to the Rate Quotes page
#    When  the user verifies fields of Rate Quotes page
#    And   click on Minimum Roundtrip Miles placeholder filter field
#    Then  the user enter a Minimum Roundtrip Miles
#    When  click on Maximum Roundtrip Miles placeholder filter field
#    Then  the user enter a Maximum Roundtrip Miles
#    And   the user click on search button under Roundtrip miles
#    And   the user should see data between Minimum Roundtrip Miles and Maiximum Roundtrip Miles only in the table
#
#  Scenario: Successful verification of filtering of Estimated Total
#    Given the user will go to the Rate Quotes page
#    When  the user verifies fields of Rate Quotes page
#    And   click on Minimum Estimated Total placeholder filter field
#    Then  the user enter a Minimum Estimated Total
#    When  click on Maximum Estimated Total placeholder filter field
#    Then  the user enter a Maximum Estimated Total
#    And   the user click on search button under Estimated Total
#    And   the user should see data between Minimum Estimated Total and Maiximum Estimated Total only in the table