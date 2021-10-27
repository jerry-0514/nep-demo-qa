from selenium import webdriver
import logging.config

logging.config.fileConfig('data/logging.ini')


def before_all(context):
    pass


def before_scenario(context, scenario):
    # initialize browser
    context.driver = webdriver.Chrome("./webdriver/chromedriver.exe")
    context.driver.maximize_window()
    context.driver.get("https://demoqa.com/login")
    context.data = {}


def after_scenario(context, scenario):
    context.driver.quit()


def after_all(context):
    pass
