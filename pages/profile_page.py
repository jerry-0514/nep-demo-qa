from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):

    nav_profile_locator = ("//*[text()='Profile']", "xpath")

    btn_logout_locator = ("//*[text()='Log out']", "xpath")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def logout_user(self):
        self.go_to_nav_bar(*self.nav_profile_locator)
        self.click_element(*self.btn_logout_locator)
        self.wait.until(EC.visibility_of_element_located((self.type_map['xpath'], "//div[text()='Login']")))
