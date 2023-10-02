from selenium import webdriver

class SeleniumDriver:
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def get_driver(self):
        return self.driver
    
    def close_driver(self):
        self.driver.quit()
