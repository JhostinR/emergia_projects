from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class SeleniumDriver:
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
    
    def get_driver(self):
        return self.driver
    
    def close_driver(self):
        self.driver.quit()
