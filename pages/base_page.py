from assertpy import assert_that
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    type_map = {"id": By.ID,
                "name": By.NAME,
                "css": By.CSS_SELECTOR,
                "xpath": By.XPATH,
                "class": By.CLASS_NAME,
                "link": By.LINK_TEXT,
                "tag": By.TAG_NAME,
                "partial_link_text": By.PARTIAL_LINK_TEXT
                }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_element(self, locator, locator_type='id'):
        self.wait.until(EC.visibility_of_element_located((self.type_map[locator_type], locator)))
        return self.find_element(locator, locator_type)

    def find_element(self, locator, locator_type='id'):
        by_type = self.type_map.get(locator_type)
        return self.driver.find_element(by_type, locator)

    def click_element(self, locator, locator_type='id'):
        logging.info("Clicking element - {}".format(locator))
        self.get_element(locator, locator_type).click()

    def get_text(self, locator, locator_type='id'):
        return self.get_element(locator, locator_type).text

    def set_field(self, value, locator, locator_type='id'):
        element = self.get_element(locator, locator_type)
        logging.info('Setting {0} with value {1}'.format(locator, value))
        element.clear()
        element.send_keys(value)

    def check_page_name(self, page_name):
        assert_that(self.get_text('main-header', 'class'), 'Check Page Name').is_equal_to(page_name)
        logging.info("Page name is {}".format(page_name))

    def wait_for_alert_message(self):
        self.wait.until(EC.alert_is_present())