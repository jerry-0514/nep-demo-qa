from assertpy import assert_that
import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


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
        self.highlight_element(self.driver.find_element(by_type, locator))
        return self.driver.find_element(by_type, locator)

    def get_elements(self, locator, locator_type='id'):
        self.wait.until(EC.visibility_of_element_located((self.type_map[locator_type], locator)))
        return self.find_elements(locator, locator_type)

    def find_elements(self, locator, locator_type='id'):
        by_type = self.type_map.get(locator_type)
        return self.driver.find_elements(by_type, locator)

    def highlight_element(self, element):
        original_style = element.get_attribute('style')
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background: yellow; border: 2px solid red;")
        time.sleep(.2)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)

    def click_element(self, locator, locator_type='id'):
        logging.info("Clicking element - {}".format(locator))
        self.wait.until(EC.element_to_be_clickable((self.type_map[locator_type], locator)))
        self.driver.execute_script("arguments[0].click();", self.get_element(locator, locator_type))

    def get_text(self, locator, locator_type='id'):
        text_value = self.get_element(locator, locator_type).text
        logging.info('Getting text for {}: {}'.format(locator, text_value))
        return text_value

    def select_by_value(self, value, locator, locator_type='id'):
        Select(self.get_element(locator, locator_type)).select_by_value(value)

    def get_attribute(self, attribute, locator, locator_type='id'):
        return self.get_element(locator, locator_type).get_attribute(attribute)

    def set_field(self, value, locator, locator_type='id'):
        element = self.get_element(locator, locator_type)
        logging.info('Setting {0} with value {1}'.format(locator, value))
        element.clear()
        element.send_keys(value)

    def go_to_nav_bar(self, locator, locator_type='id'):
        self.click_element(locator, locator_type)
        self.verify_page_is_loaded()

    def verify_page_name(self, page_name):
        assert_that(self.get_text('main-header', 'class'), 'Check Page Name').is_equal_to(page_name)
        logging.info("Page name is {}".format(page_name))

    def wait_for_alert_message(self):
        # self.wait.until(EC.alert_is_present())
        pass

    def verify_page_is_loaded(self):
        self.wait.until(EC.visibility_of_element_located((self.type_map['class'], 'main-header')))