# Created by jerry at 26-10-2021
Feature: Book Store Page
  # This contains scenarios related to book store section of the application

  Scenario: Check the completeness and correctness of records (data/books.json as data source)
    Given a logged in user
    And the user is in Book Store page
    And the user has the details of all the books from a data source
    When the user checks the details of all the books
    Then book details must be correct

  Scenario Outline: Search Functionality
    Given a logged in user
    And the user is in Book Store page
    When the user searches with search string - <search_str>
    Then all search results must contain <search_str> in <column_name>

    Examples:
    | column_name | search_str      |
    | title       | Java            |
    | title       | Git             |
    | author      | Simpson         |
    | publisher   | No Starch Press |

  Scenario: Search for non-existing record
    Given a logged in user
    And the user is in Book Store page
    When the user searches with random search string
    Then the search results must show no rows found

  Scenario Outline: Check rows per page
    Given a logged in user
    And the user is in Book Store page
    When the user changes the number of rows per page to <rows_per_page>
    Then the row count must be equal to <rows_per_page>

    Examples:
    | rows_per_page |
    | 5             |
    | 10            |
    | 20            |
    | 25            |
    | 50            |
    | 100           |
