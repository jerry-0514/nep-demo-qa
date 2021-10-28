from behave import when
from pages.profile_page import ProfilePage
from pages.navbar import NavBar


@when("the user logs out")
def when_logout_user(context):
    NavBar(context.driver).go_to_page('Profile')
    ProfilePage(context.driver).logout_user()
