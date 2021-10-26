from selenium import webdriver


def before_all(context):
    # initialize browser
    context.driver = webdriver.Chrome("./webdriver/chromedriver.exe")
    context.driver.maximize_window()
    context.driver.get("https://demoqa.com/login")


def before_scenario(context, scenario):
    context.data = {}


def after_scenario(context, scenario):
    pass


def after_all(context):
    context.driver.quit()