# Created by jerry at 26-10-2021
Feature: Login Page
  # This contains scenarios related to login and registration

  @with_manual_intervention
  Scenario: Registration of a New User
    Given a new user
    When the user registers an account
    Then the successful registration alert must be shown
    And the user must be able to use the account to login

  @functional_error
  Scenario Outline: Missing Field during Registration
    Given a new user
    When the user registers an account using the following details
      | first_name   | last_name   | user_name   | password   |
      | <first_name> | <last_name> | <user_name> | <password> |
    Then a warning icon must be shown for <null_field> field

    Examples:
    | first_name | last_name | user_name  | password  | null_field |
    |            | Smith     | null_smith | Passw0rd! | first_name |
    | Ed         |           | ed_null    | Passw0rd! | last_name  |
    | Ed         | Smith     |            | Passw0rd! | user_name  |
    | Ed         | Smith     | ed.smith   |           | password   |

  @functional_error
  Scenario: Registration without Captcha
    Given a new user
    When the user registers an account without captcha
    Then an error message related to captcha must be shown

  @functional_error @with_manual_intervention
  Scenario Outline: Invalid Password during Registration
    Given a new user
    When the user registers an account using password - <password>
    Then an error message related to password must be shown

    Examples:
    | password        |
    | allsmallletters |
    | short           |
    | ALLCAPCHARS     |
    | N0SpecialChar   |
    | 12345678        |

  Scenario: Successful Login for an existing user
    Given an existing user
    When the user logs in using the correct credentials
    Then the user must be redirected to Profile page

  @functional_error
  Scenario: Login using invalid password
    Given an existing user
    When the user logs in using the incorrect password
    Then an error message related to invalid credentials must be shown

  @functional_error
  Scenario: Login using non-existing account
    Given a new user
    When the user logs in using random credentials
    Then an error message related to invalid credentials must be shown

  Scenario: Logout User
    Given an existing user
    And the user has successfully logged in
    When the user logs out
    Then the user must be redirected to Login page