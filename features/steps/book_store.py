import logging
from behave import when, then
from faker import Faker
from assertpy import assert_that
from pages.book_store_page import BookStorePage


@when("the user checks the details of all the books")
def get_book_details_from_the_site(context):
    context.results['book_details'] = BookStorePage(context.driver).get_book_details()


@when("the user searches with search string - {search_str}")
def when_user_search(context, search_str):
    BookStorePage(context.driver).search_book(search_str)


@when("the user searches with random search string")
def when_user_search_randomly(context):
    BookStorePage(context.driver).search_book(Faker().name())


@when("the user changes the number of rows per page to {rows_per_page}")
def when_select_row_per_page(context, rows_per_page):
    BookStorePage(context.driver).set_rows_per_page(rows_per_page)


@then("book details must be correct")
def validate_book_details(context):
    logging.info('Actual Results: {}'.format(context.results['book_details']))
    logging.info('Expected Results: {}'.format(context.data['book_details']))
    for book in context.results['book_details']:
        assert_that(context.data['book_details']).contains(book)


@then("all search results must contain {search_str} in {column_name}")
def validate_search_results(context, search_str, column_name):
    BookStorePage(context.driver).verify_search_results(search_str, column_name)


@then("the search results must show no rows found")
def validate_no_search_results(context):
    BookStorePage(context.driver).verify_no_search_results()


@then("the row count must be equal to {rows_per_page}")
def validate_row_count(context, rows_per_page):
    BookStorePage(context.driver).verify_row_count(rows_per_page)