Feature: Market Search
  Scenario: Search for smartphones within specified parameters and check rating
    Given the Yandex.Market website is opened
    When I go to the Catalog section
    And I select "Electronics" and "Smartphones"
    And I go to "All Filters"
    And I set the search parameters for price and screen size
    And I select 5 manufacturers
    And I click the "Show" button
    Then I count the number of smartphones on the page
    And I remember the last smartphone from the list
    And I change the sorting to "by discount"
    And I click on the remembered smartphone
    Then I check the rating of the selected product