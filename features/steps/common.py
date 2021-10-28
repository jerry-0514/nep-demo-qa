import pyautogui
import time
import json

from behave import given, then
from faker import Faker
from pages.base_page import BasePage
from pages.navbar import NavBar

from features.steps.login import login_user


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


@given("a logged in user")
def logged_in_user(context):
    use_existing_user(context)
    login_user(context, username=context.data['user_name'], password=context.data['password'])


@given("the user is in {page_name} page")
def go_to_page(context, page_name):
    NavBar(context.driver).go_to_page(page_name)


@given("the user has the details of all the books from a data source")
def parse_book_details_from_data_source(context):
    f = open('data/books.json', encoding="utf-8")
    context.data['book_details'] = json.load(f)
    f.close()


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
