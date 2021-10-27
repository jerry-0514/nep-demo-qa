from assertpy import assert_that
from behave import when, then, given
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def login_user(context, username, password, is_successful=True):
    LoginPage(context.driver).login_user(username, password, is_successful)


def register_user(context, first_name, last_name, user_name, password, captcha=True):
    LoginPage(context.driver).go_to_register_page()
    RegisterPage(context.driver).register_user(first_name, last_name, user_name, password, captcha)


@when("the user registers an account")
def when_register_user(context):
    register_user(context, context.data['first_name'], context.data['last_name'],
                  context.data['user_name'], context.data['password'])


@when("the user registers an account using the following details")
def when_register_with_predefined_details(context):
    register_user(context, **dict(zip(context.table.headings, context.table.rows[0].cells)), captcha=False)


@when("the user registers an account using password - {password}")
def when_register_with_predefined_password(context, password):
    register_user(context, context.data['first_name'], context.data['last_name'],
                  context.data['user_name'], password)


@when("the user registers an account without captcha")
def when_register_without_captcha(context):
    register_user(context, context.data['first_name'], context.data['last_name'],
                  context.data['user_name'], context.data['password'], captcha=False)


@when("the user logs in using the correct credentials")
def when_login_user(context):
    login_user(context, username=context.data['user_name'], password=context.data['password'])


@when("the user logs in using the incorrect password")
def when_login_user_with_incorrect_password(context):
    login_user(context, username=context.data['user_name'], password='Rand0mpw!', is_successful=False)


@when("the user logs in using random credentials")
def when_login_with_no_account(context):
    login_user(context, username=context.data['user_name'], password=context.data['password'], is_successful=False)


@given("the user has successfully logged in")
@then("the user must be able to use the account to login")
def verify_user_can_login(context):
    login_user(context, username=context.data['user_name'], password=context.data['password'])
    LoginPage(context.driver).verify_successful_login()


@then("a warning icon must be shown for {null_field} field")
def verify_missing_field_icon(context, null_field):
    locator_map = {
        'first_name': RegisterPage.txt_first_name_locator,
        'last_name': RegisterPage.txt_last_name_locator,
        'user_name': RegisterPage.txt_user_name_locator,
        'password': RegisterPage.txt_password_locator
    }
    cls_attribute = BasePage(context.driver).get_attribute('class', *locator_map[null_field])
    assert_that(cls_attribute, '').contains('is-invalid')


@then("an error message related to captcha must be shown")
def verify_captcha_error(context):
    err_msg = RegisterPage(context.driver).get_error_message()
    assert_that(err_msg).is_equal_to('Please verify reCaptcha to register!')


@then("an error message related to password must be shown")
def verify_password_error(context):
    err_msg = RegisterPage(context.driver).get_error_message()
    assert_that(err_msg).is_equal_to(
        "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), "
        "one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.")


@then("an error message related to invalid credentials must be shown")
def verify_login_error(context):
    err_msg = LoginPage(context.driver).get_error_message()
    assert_that(err_msg).is_equal_to("Invalid username or password!")
