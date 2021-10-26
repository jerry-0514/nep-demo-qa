# Created by jerry at 26-10-2021
Feature: Book Store Page
  # This contains scenarios related to book store section of the application

  Scenario: Check the completeness and correctness of records (data/books.json as data source)
    Given an existing user
    And the user is in Book Store page
    When the user checks all the book records
    Then the book details must be correct

  Scenario Outline: Search Functionality
    Given an existing user
    And the user is in Book Store page
    When the user searches by <column_name> with search string - <search_str>
    Then the all search results must contain <search_str> in <column_name>

    Examples:
    | column_name | search_str      |
    | Title       | Java            |
    | Title       | Git             |
    | Author      | Simpson         |
    | Publisher   | No Starch Press |

  Scenario: Search for non-existing record
    Given an existing user
    And the user is in Book Store page
    When the user searches with random search string
    Then the search results must show no rows found

  Scenario Outline: Check rows per page
    Given an existing user
    And the user is in Book Store page
    When the user changes the number of rows per page to <rows_per_page>
    Then the search results count must be equal or less than <rows_per_page>

    Examples:
    | rows_per_page |
    | 5             |
    | 10            |
    | 20            |
    | 25            |
    | 50            |
    | 100           |

  Scenario Outline: Check rows per page
    Given an existing user
    And the user is in Book Store page
    When the user changes the number of rows per page to <rows_per_page>
    Then the search results count must be equal or less than <rows_per_page>

    Examples:
    | rows_per_page |
    | 5             |
    | 10            |
    | 20            |
    | 25            |
    | 50            |
    | 100           |
