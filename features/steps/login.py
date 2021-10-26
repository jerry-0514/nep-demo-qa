import logging
from assertpy import assert_that
from behave import when, then
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@when("the user registers an account")
def register_account(context):
    LoginPage(context.driver).go_to_register_page()
    RegisterPage(context.driver).register_user(
        first_name=context.data['first_name'],
        last_name=context.data['last_name'],
        username=context.data['user_name'],
        password=context.data['password']
    )


# WIP: it seems that selenium cant switch to the alert
@then("the {alert_type} alert must be shown")
def verify_alert(context, alert_type):
    alert_type_dict = {
        'successful registration': 'User Register Successfully.'
    }
    alert_e = context.driver.switch_to.alert
    alert_msg = alert_e.text
    logging.info("Alert says {}".format(alert_msg))
    assert_that(alert_msg).is_equal_to(alert_type_dict[alert_type])
    alert_e.accept()
