from behave import given
from faker import Faker


@given("a new user")
def create_new_user(context):
    context.data['first_name'] = Faker().first_name()
    context.data['last_name'] = Faker().last_name()
    context.data['user_name'] = context.data['first_name'].lower() + context.data['last_name'].lower()
    context.data['password'] = 'Passw0rd!'


@given("an existing user")
def use_existing_user(context):
    context.data['first_name'] = 'Timothy'
    context.data['last_name'] = 'Baker'
    context.data['user_name'] = 'timothy.baker'
    context.data['password'] = "Passw0rd!"

