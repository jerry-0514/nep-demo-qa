from pages.base_page import BasePage
from assertpy import assert_that

import logging


class BookStorePage(BasePage):

    txt_search_locator = ("searchBox", "id")

    link_title_locator = ("//span[@class='mr-2']", "xpath")
    lbl_author_locator = ("//*[@class='rt-tr-group']//div[3]", "xpath")
    lbl_publisher_locator = ("//*[@class='rt-tr-group']//div[4]", "xpath")

    comp_row_locator = ("//*[@class='rt-tr-group']", "xpath")

    lbl_empty_locator = ("//*[text()='No rows found']", "xpath")

    comp_profile_wrapper_locator = ("//*[@class='profile-wrapper']", "xpath")
    lbl_detail_field_locator = ("//div[@class='mt-2 row'][{}]/child::div[1]", "xpath")
    lbl_detail_value_locator = ("//div[@class='mt-2 row'][{}]/child::div[2]", "xpath")

    btn_back_locator = ("//*[text()='Back To Book Store']", "xpath")
    btn_search_locator = ("basic-addon2", "id")

    drp_rows_locator = ("//*[@aria-label='rows per page']", "xpath")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_book_details(self):
        titles = [title_e.text for title_e in self.get_elements(*self.link_title_locator)]
        book_details = []
        for title in titles:
            logging.info('Checking the details of the book: {}'.format(title))
            self.click_element('//*[text()="{}"]'.format(title), 'xpath')
            self.get_element(*self.comp_profile_wrapper_locator)
            row_count = len(self.get_elements("//div[@class='mt-2 row']", "xpath"))
            book_details.append({
                self.get_text(self.lbl_detail_field_locator[0].format(str(ctr)),
                              'xpath').replace(' :', '').replace(' ', '_').lower():
                    self.get_text(self.lbl_detail_value_locator[0].format(str(ctr)), 'xpath')
                for ctr in range(1, row_count + 1)})
            self.click_element(*self.btn_back_locator)
        return book_details

    def search_book(self, search_str):
        self.set_field(search_str, *self.txt_search_locator)
        self.click_element(*self.btn_search_locator)

    def verify_search_results(self, search_str, column):
        locator_column_mapping = {
            "title": self.link_title_locator,
            "author": self.lbl_author_locator,
            "publisher": self.lbl_publisher_locator
        }
        search_results = [e.text for e in self.get_elements(*locator_column_mapping[column]) if e.text != ' ']
        logging.info('{} results found!'.format(str(len(search_results))))
        for res in search_results:
            logging.info('Checking {} contains {}.'.format(res, search_str))
            assert_that(res).contains(search_str)

    def verify_no_search_results(self):
        e = self.get_element(*self.lbl_empty_locator)
        logging.info('No search results found!')

    def set_rows_per_page(self, row_cnt):
        self.select_by_value(row_cnt, *self.drp_rows_locator)

    def verify_row_count(self, row_cnt):
        actual_row_cnt = len(self.get_elements(*self.comp_row_locator))
        assert_that(actual_row_cnt).is_equal_to(int(row_cnt))