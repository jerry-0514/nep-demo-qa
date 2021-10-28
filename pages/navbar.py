from pages.base_page import BasePage


class NavBar(BasePage):

    nav_login_locator = ("//span[text()='{}']", "xpath")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_page(self, page_name):
        self.go_to_nav_bar(self.nav_login_locator[0].format(page_name), self.nav_login_locator[1])