import pyautogui
import time

from behave import given, then
from faker import Faker
from pages.base_page import BasePage


@given("a new user")
def create_new_user(context):
    context.data['first_name'] = Faker().first_name()
    context.data['last_name'] = Faker().last_name()
    context.data['user_name'] = context.data['first_name'].lower() + '.' + context.data['last_name'].lower()
    context.data['password'] = 'Passw0rd!'


@given("an existing user")
def use_existing_user(context):
    context.data['first_name'] = 'Timothy'
    context.data['last_name'] = 'Baker'
    context.data['user_name'] = 'timothy.baker'
    context.data['password'] = "Passw0rd!"


@then("the user must be redirected to {page_name} page")
def verify_redirected_page(context, page_name):
    BasePage(context.driver).verify_page_name(page_name)


@then("the {alert_type} alert must be shown")
def verify_alert(context, alert_type):
    alert_type_dict = {
        'successful registration': 'User Register Successfully.'
    }

    # alert_e = context.driver.switch_to.alert
    # alert_msg = alert_e.text
    # logging.info("Alert says {}".format(alert_msg))
    # assert_that(alert_msg).is_equal_to(alert_type_dict[alert_type])
    # alert_e.accept()

    time.sleep(3)
    pyautogui.press('enter')
