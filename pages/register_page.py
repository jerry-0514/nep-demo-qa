from pages.base_page import BasePage
import pyautogui
import time


class RegisterPage(BasePage):

    txt_first_name_locator = ("firstname", "id")
    txt_last_name_locator = ("lastname", "id")
    txt_user_name_locator = ("userName", "id")
    txt_password_locator = ("password", "id")

    btn_register_locator = ("register", "id")
    btn_back_to_login_locator = ("gotologin", "id")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def register_user(self, first_name, last_name, username, password):
        self.set_field(first_name, *self.txt_first_name_locator)
        self.set_field(last_name, *self.txt_last_name_locator)
        self.set_field(username, *self.txt_user_name_locator)
        self.set_field(password, *self.txt_password_locator)
        pyautogui.alert('Please answer the captcha first before clicking OK. Thank you!', 'Oops! I dont know Captcha.')
        self.click_element(*self.btn_register_locator)
        # self.wait_for_alert_message()
