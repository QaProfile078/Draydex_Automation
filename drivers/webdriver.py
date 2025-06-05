from selenium import webdriver

def create_webdriver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
