from behave import when
from pages.profile_page import ProfilePage


@when("the user logs out")
def when_logout_user(context):
    ProfilePage(context.driver).logout_user()
