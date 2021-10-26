from pages.base_page import BasePage


class LoginPage(BasePage):

    txt_user_name_locator = ("userName", "id")
    txt_password_locator = ("password", "id")

    btn_login_locator = ("login", "id")
    btn_register_locator = ("newUser", "id")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_register_page(self):
        self.click_element(*self.btn_register_locator)
        self.check_page_name('Register')
