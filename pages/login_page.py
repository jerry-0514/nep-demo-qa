from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    nav_login_locator = ("//*[text()='Login']", "xpath")

    txt_user_name_locator = ("userName", "id")
    txt_password_locator = ("password", "id")

    btn_login_locator = ("login", "id")
    btn_register_locator = ("newUser", "id")

    err_msg_locator = ("//p[@id='name']", "xpath")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_user(self, username, password, is_successful=True):
        self.go_to_nav_bar(*self.nav_login_locator)

        self.set_field(username, *self.txt_user_name_locator)
        self.set_field(password, *self.txt_password_locator)

        self.click_element(*self.btn_login_locator)
        if is_successful:
            self.wait.until(EC.visibility_of_element_located((self.type_map['xpath'], "//div[text()='Profile']")))

    def verify_successful_login(self):
        self.verify_page_name('Profile')

    def go_to_register_page(self):
        self.click_element(*self.btn_register_locator)
        self.verify_page_name('Register')

    def get_error_message(self):
        return self.get_text(*self.err_msg_locator)
