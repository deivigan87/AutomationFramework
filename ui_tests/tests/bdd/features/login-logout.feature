Feature: Login and logout functionality validation
  Set of tests for login and logout functionality validation

  Scenario: Login and logout via SmartPass
    When I click user icon
    And I click SmartPass button
    And I set 'persona.user65' login and 'P@ssword123' password
    And I click login button
    And I click logged user icon
    Then Profile icon is present
    When I click logout button
    Then Guest user icon is present
    When I click user icon
    Then Profile icon is absent
    And SmartPass button is present