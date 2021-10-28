import logging

from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):

    link_title_locator = ("//span[@class='mr-2']", "xpath")
    link_first_title_locator = ("//span[@class='mr-2'][1]", "xpath")

    first_icon_delete_locator = ("//*[@class='rt-tr-group'][1]//*[@id='delete-record-undefined']", "xpath")
    lbl_empty_locator = ("//*[text()='No rows found']", "xpath")

    btn_logout_locator = ("//*[text()='Log out']", "xpath")
    btn_delete_all_books_locator = ("//*[text()='Delete All Books']", "xpath")
    btn_goto_store_locator = ("gotoStore", "id")

    btn_confirm_delete_locator = ("closeSmallModal-ok", "id")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_book_store(self):
        self.click_element(*self.btn_goto_store_locator)

    def logout_user(self):
        self.click_element(*self.btn_logout_locator)
        self.wait.until(EC.visibility_of_element_located((self.type_map['xpath'], "//div[text()='Login']")))

    def verify_book_in_collection(self, title):
        self.get_element('//*[text()="{}"]'.format(title), 'xpath')
        logging.info('{} is in the collection'.format(title))

    def count_books_in_collection(self):
        try:
            return len(self.get_elements(*self.link_title_locator))
        except TimeoutException:
            return 0

    def delete_first_book(self):
        title = self.get_text(*self.link_first_title_locator)
        logging.info('Deleting this book: {}'.format(title))
        self.click_element(*self.first_icon_delete_locator)
        self.click_element(*self.btn_confirm_delete_locator)
        return title

    def verify_book_is_deleted(self, title):
        try:
            self.get_element('//*[text()="{}"]'.format(title), 'xpath')
            raise AssertionError
        except AttributeError:
            logging.info('{} book is not found in the collection.'.format(title))
            return

    def delete_all_books(self):
        logging.info('Deleting all books!')
        self.click_element(*self.btn_delete_all_books_locator)
        self.click_element(*self.btn_confirm_delete_locator)

    def verify_no_search_results(self):
        e = self.get_element(*self.lbl_empty_locator)
        logging.info('No search results found!')
