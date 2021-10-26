# Created by jerry at 26-10-2021
Feature: Profile Page
  # This contains scenarios related to profile of the user

  Scenario: Redirection to Book Store page from Profile page
    Given an existing user
    And the user is in Profile page
    When the user clicks the Go To Book Store button
    Then the user must be redirected to Book Store page

  Scenario: Add a book to the collection
    Given an existing user
    And the user is in Book Store page
    And the user selects a random book
    When the user adds the book to the collection
    Then the successful book added alert must be shown
    And the book must be shown in the user's collection in Profile page

  Scenario: Delete a book from the collection
    Given an existing user with at least one book/s in the collection
    When the user deletes the first book from the collection
    Then the successful book deletion alert must be shown
    And the book must not be shown in the user's collection in Profile page

  Scenario: Delete all books from an empty collection
    Given an existing user with at least two book/s in the collection
    When the user deletes all books from the collection
    Then the no books available alert must be shown
    Then the collection must show no rows found

  @functional_error
  Scenario: Delete all books from an empty collection
    Given a newly registered user
    When the user deletes all books from the collection
    Then the all books deleted alert must be shown

  Scenario: Delete Account
    Given a newly registered user
    When the user deletes the account
    Then the successful account deletion alert must be shown
    And user must not be able to login