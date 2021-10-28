from behave import given, when, then

from features.steps.book_store import given_select_random_book
from features.steps.common import logged_in_user, verify_alert
from pages.profile_page import ProfilePage
from pages.book_store_page import BookStorePage
from pages.navbar import NavBar


def add_book_to_collection(context):
    NavBar(context.driver).go_to_page('Book Store')
    given_select_random_book(context)
    BookStorePage(context.driver).add_book_to_collection()
    verify_alert(context)
    validate_book_is_added(context)


@given("an existing user with at least {count} book/s in the collection")
def user_with_existing_collection(context, count):
    logged_in_user(context)
    book_cnt = ProfilePage(context.driver).count_books_in_collection()
    if book_cnt < int(count):
        for ctr in range(0, int(count) - book_cnt):
            add_book_to_collection(context)


@given("a logged in user with no collection")
def registered_user(context):
    logged_in_user(context)
    book_cnt = ProfilePage(context.driver).count_books_in_collection()
    if book_cnt > 0:
        when_delete_all_books(context)
        verify_alert()
        validate_no_rows(context)


@when("the user logs out")
def when_logout_user(context):
    NavBar(context.driver).go_to_page('Profile')
    ProfilePage(context.driver).logout_user()


@when("the user clicks the Go To Book Store button")
def when_go_to_book_store(context):
    ProfilePage(context.driver).navigate_to_book_store()


@when("the user adds the book to the collection")
def when_add_to_collection(context):
    BookStorePage(context.driver).add_book_to_collection()


@when("the user deletes the first book from the collection")
def when_delete_first_book(context):
    context.data['recently_deleted_book'] = ProfilePage(context.driver).delete_first_book()


@when("the user deletes all books from the collection")
def when_delete_all_books(context):
    NavBar(context.driver).go_to_page('Profile')
    ProfilePage(context.driver).delete_all_books()


@then("the book must be shown in the user's collection in Profile page")
def validate_book_is_added(context):
    NavBar(context.driver).go_to_page('Profile')
    ProfilePage(context.driver).verify_book_in_collection(context.data['recently_added_book'])


@then("the book must not be shown in the user's collection in Profile page")
def validate_book_is_deleted(context):
    ProfilePage(context.data).verify_book_is_deleted(context.data['recently_deleted_book'])


@then("the collection must show no rows found")
def validate_no_rows(context):
    ProfilePage(context.driver).verify_no_search_results()